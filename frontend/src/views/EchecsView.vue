<template>
  <section class="mx-auto max-w-2xl">
    <div class="mb-4 flex items-center justify-between gap-3">
      <RouterLink
        to="/"
        class="rounded-full bg-white px-4 py-2 text-sm font-extrabold text-[#6d28d9] shadow-sm transition-shadow hover:shadow-md"
      >
        ← Accueil
      </RouterLink>
      <h1 class="text-2xl font-extrabold text-[#6d28d9]">Échecs</h1>
      <span class="text-sm font-bold text-amber-700">⭐ {{ progression.etoiles }}</span>
    </div>

    <div class="rounded-3xl bg-white p-5 shadow-sm sm:p-7">
      <p class="mb-4 text-center text-[0.95rem] font-bold text-[#3f3556]">
        Tu joues les <span class="text-[#6d28d9]">pièces blanches</span> ⟶ capture le roi violet de Milo !
      </p>

      <!-- Tour de jeu -->
      <p class="mb-3 text-center text-[0.95rem] font-extrabold" :class="tonTour ? 'text-[#6d28d9]' : 'text-amber-700'">
        {{ fin ? '' : tonTour && !selection ? 'Sélectionne une pièce blanche...' : MiloRaisonner ? '🤖 Milo réfléchit...' : '' }}
      </p>

      <!-- Plateau -->
      <div class="mx-auto w-fit rounded-2xl border-4 border-[#6d28d9] overflow-hidden">
        <div v-for="l in 8" :key="l" class="flex">
          <button
            v-for="c in 8"
            :key="c"
            class="flex h-10 w-10 items-center justify-center text-[1.55rem] leading-none transition-colors sm:h-12 sm:w-12 sm:text-[1.8rem]"
            :class="[
              (l + c) % 2 === 0 ? 'bg-[#dcd0f7]' : 'bg-[#f5f1ff]',
              cible(l - 1, c - 1) ? 'ring-2 ring-inset ring-[#22c55e]' : '',
              selection && selection[0] === l - 1 && selection[1] === c - 1 ? 'ring-2 ring-inset ring-[#6d28d9]' : '',
            ]"
            @click="cliquer(l - 1, c - 1)"
          >
            <span v-if="piece(l - 1, c - 1)" :class="couleurPiece(l - 1, c - 1)">{{ piece(l - 1, c - 1) }}</span>
          </button>
        </div>
      </div>

      <!-- Message / fin -->
      <p v-if="fin" class="mt-4 text-center text-[1.2rem] font-extrabold" :class="gagne ? 'text-green-600' : 'text-rose-500'">
        {{ messageFin }}
      </p>

      <div class="mt-5 flex justify-center gap-3">
        <button
          class="rounded-full bg-[#6d28d9] px-8 py-3 font-extrabold text-white transition-transform hover:scale-105"
          @click="recommencer"
        >
          {{ fin ? 'Rejouer' : 'Commencer' }}
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { progression, noterScore } from '../stores/progression'

/* Échecs pour les petits : vraies règles de déplacement, sans échec/mat.
   Gagner = capturer le roi adverse. Milo (noirs) joue ses meilleurs coups. */

const GLYPHS = {
  K: '♔', Q: '♕', R: '♖', B: '♗', N: '♘', P: '♙',
  k: '♚', q: '♛', r: '♜', b: '♝', n: '♞', p: '♟',
}
const VALEURS = { k: 100, q: 9, r: 5, b: 3, n: 3, p: 1, '.': 0 }

const plateau = ref([])
const selection = ref(null)
const cibles = ref([])
const tonTour = ref(true)
const MiloRaisonner = ref(false)
const fin = ref(false)
const gagne = ref(false)
const messageFin = ref('')
const pointsCoups = ref(0)

const piece = (l, c) => (plateau.value[l]?.[c] && plateau.value[l][c] !== '.' ? GLYPHS[plateau.value[l][c]] : '')
const couleurPiece = (l, c) =>
  plateau.value[l][c] === plateau.value[l][c].toUpperCase() ? 'text-slate-900 drop-shadow-[0_1px_0_white]' : 'text-[#6d28d9]'
const cible = (l, c) => cibles.value.some(([x, y]) => x === l && y === c)

/* Coups possibles selon la pièce (théorie des déplacements simple). */
function casesLegales(l, c) {
  const p = plateau.value[l][c]
  if (!p || p === '.') return []
  const blanc = p === p.toUpperCase()
  const resultat = []
  const libre = (x, y) => x >= 0 && x < 8 && y >= 0 && y < 8 && plateau.value[x][y] === '.'
  const prend = (x, y) =>
    x >= 0 && x < 8 && y >= 0 && y < 8 && plateau.value[x][y] !== '.' &&
    blanc !== (plateau.value[x][y] === plateau.value[x][y].toUpperCase())

  const direction = (pas) => {
    for (const [dx, dy] of pas) {
      let x = l + dx
      let y = c + dy
      // pour les lignes à portée infinie
      const infinie = ['R', 'r', 'B', 'b', 'Q', 'q'].includes(p)
      if (infinie) {
        while (libre(x, y)) {
          resultat.push([x, y])
          x += dx
          y += dy
        }
        if (prend(x, y)) resultat.push([x, y])
      } else if (libre(x, y) || prend(x, y)) {
        resultat.push([x, y])
      }
    }
  }

  if (p === 'N' || p === 'n') {
    for (const [dx, dy] of [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]) {
      if (libre(l + dx, c + dy) || prend(l + dx, c + dy)) resultat.push([l + dx, c + dy])
    }
  } else if (p === 'R' || p === 'r') {
    direction([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]])
  } else if (p === 'B' || p === 'b') {
    direction([[1, 1], [1, -1], [-1, 1], [-1, -1]])
  } else if (p === 'Q' || p === 'q') {
    direction([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]])
  } else if (p === 'K' || p === 'k') {
    direction([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]])
  } else if (p === 'P' || p === 'p') {
    const avantage = blanc ? -1 : 1
    if (libre(l + avantage, c)) {
      resultat.push([l + avantage, c])
      const depart = blanc ? 6 : 1
      if (l === depart && libre(l + 2 * avantage, c)) resultat.push([l + 2 * avantage, c])
    }
    for (const dy of [-1, 1]) {
      if (prend(l + avantage, c + dy)) resultat.push([l + avantage, c + dy])
    }
  }

  return resultat.filter(([x, y]) => !(x === l && y === c))
}

function cliquer(l, c) {
  if (fin.value || !tonTour.value) return
  const p = plateau.value[l]?.[c] || '.'
  const dejaSelectionnee = selection.value && selection.value[0] === l && selection.value[1] === c
  if (dejaSelectionnee) {
    selection.value = null
    cibles.value = []
    return
  }
  // Une pièce blanche : on la sélectionne.
  if (p !== '.' && p === p.toUpperCase()) {
    selection.value = [l, c]
    cibles.value = casesLegales(l, c)
    return
  }
  // Une cible : on joue.
  if (selection.value && cibles.value.some(([x, y]) => x === l && y === c)) {
    avancer(selection.value, [l, c])
  }
}

function avancer(de, vers) {
  const [xl, xc] = de
  const [vl, vc] = vers
  const nouveau = plateau.value.map((rangée) => [...rangée])
  let p = nouveau[xl][xc]
  // promotion du pion
  if (p === 'P' && vl === 0) p = 'Q'
  nouveau[vl][vc] = p
  nouveau[xl][xc] = '.'
  plateau.value = nouveau
  selection.value = null
  cibles.value = []
  pointsCoups.value += 2

  if (finDePartie(nouveau)) return
  tonTour.value = false
  MiloRaisonner.value = true
  setTimeout(coupMilo, 700)
}

function finDePartie(g) {
  if (!g.flat().includes('k')) {
    fin.value = true
    gagne.value = true
    messageFin.value = 'Bravo ! Roi de Milo capturé 🎉'
    const etoiles = pointsCoups.value <= 30 ? 3 : pointsCoups.value <= 60 ? 2 : 1
    noterScore('echecs', progression.niveau, pointsCoups.value * 10, etoiles)
    return true
  }
  if (!g.flat().includes('K')) {
    fin.value = true
    gagne.value = false
    messageFin.value = 'Milo a capturé ton roi ! Essaie encore.'
    return true
  }
  return false
}

/* Milo : ici il cherche le meilleur coup possible (capture la plus grosse pièce). */
function coupMilo() {
  const coups = []
  for (let l = 0; l < 8; l += 1) {
    for (let c = 0; c < 8; c += 1) {
      const p = plateau.value[l][c]
      if (p !== '.' && p === p.toLowerCase()) {
        for (const dest of casesLegales(l, c)) coups.push({ de: [l, c], vers: dest, piece: p })
      }
    }
  }
  if (coups.length === 0) {
    MiloRaisonner.value = false
    tonTour.value = true
    return
  }
  const cible = ([vl, vc]) => VALEURS[plateau.value[vl][vc]] || 0
  coups.sort((a, b) => cible(b.vers) - cible(a.vers))
  const meilleur = coups[0]
  avancerMilo(meilleur.de, meilleur.vers)
}

function avancerMilo(de, vers) {
  const [xl, xc] = de
  const [vl, vc] = vers
  const nouveau = plateau.value.map((rangée) => [...rangée])
  let p = nouveau[xl][xc]
  if (p === 'p' && vl === 7) p = 'q'
  nouveau[vl][vc] = p
  nouveau[xl][xc] = '.'
  plateau.value = nouveau
  MiloRaisonner.value = false
  tonTour.value = true
  if (finDePartie(nouveau)) return
  // aucune pièce blanche jouable = partie finie
  const jouable = nouveau.some((rangée, l) =>
    rangée.some((pc, c) => pc !== '.' && pc === pc.toUpperCase() && casesLegales(l, c).length > 0),
  )
  if (!jouable) {
    fin.value = true
    gagne.value = false
    messageFin.value = "Tu n'as plus de coups ! Essaie encore."
  }
}

function recommencer() {
  const vide = () => Array(8).fill('.')
  const g = Array.from({ length: 8 }, vide)
  g[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
  g[1] = Array(8).fill('p')
  g[6] = Array(8).fill('P')
  g[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
  plateau.value = g
  selection.value = null
  cibles.value = []
  fin.value = false
  gagne.value = false
  messageFin.value = ''
  tonTour.value = true
  pointsCoups.value = 0
}

recommencer()
</script>

<style scoped>
.cible {
  box-shadow: inset 0 0 0 3px #22c55e;
}
</style>

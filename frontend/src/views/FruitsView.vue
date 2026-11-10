<template>
  <section class="jeu">
    <h1 class="titre-jeu">Fusion des Fruits</h1>

    <p v-if="erreur" class="message-erreur">
      {{ erreur }}<br />
      <button class="btn-gros" @click="demarrer">Réessayer</button>
    </p>

    <template v-if="etape === 'accueil'">
      <p class="rappel-niveau">
        Fais glisser le plateau : deux fruits identiques fusionnent en un fruit plus gros.
        La mini-fraise au début, la pastèque à la fin !
      </p>
      <button class="btn-gros" @click="demarrer">C'est parti !</button>
    </template>

    <template v-else-if="etape === 'jeu'">
      <div class="chaine-fruits">
        <span
          v-for="(fruit, i) in CHAINE"
          :key="i"
          :class="{ 'est-atteint': i <= meilleurFruit }"
          :title="fruit"
        >{{ fruit }}</span>
      </div>
      <p class="compteur">Score : {{ score }}</p>

      <div
        class="plateau-fruits"
        :style="{ '--colonnes-fruits': taille }"
        @touchstart.prevent="debutToucher"
        @touchend.prevent="finToucher"
      >
        <div
          v-for="(fruit, index) in grille"
          :key="index"
          class="case-fruit"
          :class="{ 'est-pleine': fruit !== null }"
        >
          <span v-if="fruit !== null">{{ CHAINE[fruit] }}</span>
        </div>
      </div>

      <div class="fleches-fruits">
        <button class="btn-fleche" aria-label="Vers le haut" @click="jouerCoup('haut')">↑</button>
        <div class="rangee-fleches">
          <button class="btn-fleche" aria-label="Vers la gauche" @click="jouerCoup('gauche')">←</button>
          <button class="btn-fleche" aria-label="Vers le bas" @click="jouerCoup('bas')">↓</button>
          <button class="btn-fleche" aria-label="Vers la droite" @click="jouerCoup('droite')">→</button>
        </div>
      </div>
      <p class="rappel-niveau">Tu peux aussi glisser le doigt sur le plateau (ou les flèches du clavier).</p>
    </template>

    <template v-else-if="etape === 'fin'">
      <div class="carte-gagnant" v-if="gagne">
        <p class="etoiles-grandes">{{ '★'.repeat(3) }}</p>
        <p class="fruit-final">{{ CHAINE[INDEX_PASTEQUE] }}</p>
        <p class="score-final">Score : {{ score }} points</p>
        <p class="bravo">La pastèque est arrivée, champion !</p>
      </div>
      <div class="carte-gagnant" v-else>
        <p class="etoiles-grandes">{{ '★'.repeat(1) + '☆'.repeat(2) }}</p>
        <p class="score-final">Score : {{ score }} points</p>
        <p class="bravo">Plus de place... Essaie à nouveau !</p>
      </div>
      <div class="rangee-boutons">
        <button class="btn-gros" @click="demarrer">Rejouer</button>
        <RouterLink to="/" class="btn-lien">Maison</RouterLink>
      </div>
    </template>
  </section>
</template>

<script setup>
import { onMounted, onUnmounted, ref, watch } from 'vue'
import { RouterLink } from 'vue-router'
import API from '../api'
import { progression, noterScore } from '../stores/progression'

const CHAINE = ['🍓', '🍇', '🍋', '🍊', '🍎', '🍑', '🍍', '🥥', '🍈', '🍉']
const INDEX_PASTEQUE = CHAINE.length - 1

const etape = ref('accueil')
const erreur = ref('')
const grille = ref([])
const taille = ref(4)
const score = ref(0)
const meilleurFruit = ref(0)
const gagne = ref(false)

/* --- Lancement ---------------------------------------------------------- */
function demarrer() {
  erreur.value = ''
  taille.value = progression.niveau === 1 ? 3 : 4
  grille.value = Array(taille.value * taille.value).fill(null)
  score.value = 0
  meilleurFruit.value = 0
  gagne.value = false
  etape.value = 'jeu'
  spawn()
  spawn()
  spawn()
}

function spawn() {
  const vides = grille.value
    .map((v, i) => (v === null ? i : null))
    .filter((i) => i !== null)
  if (!vides.length) return
  const position = vides[Math.floor(Math.random() * vides.length)]
  grille.value[position] = Math.random() < 0.7 ? 0 : 1
}

/* --- Déplacements (façon 2048) ------------------------------------------ */
function lignesDeDirection(direction) {
  const n = taille.value
  const lignes = []
  for (let i = 0; i < n; i += 1) {
    const indices = []
    for (let j = 0; j < n; j += 1) {
      if (direction === 'gauche') indices.push(i * n + j)
      if (direction === 'droite') indices.push(i * n + (n - 1 - j))
      if (direction === 'haut') indices.push(j * n + i)
      if (direction === 'bas') indices.push((n - 1 - j) * n + i)
    }
    lignes.push(indices)
  }
  return lignes
}

function deplacer(direction) {
  let aBouge = false
  let pointsGagnes = 0
  for (const indices of lignesDeDirection(direction)) {
    const fruits = indices.map((i) => grille.value[i]).filter((v) => v !== null)
    const fusionnes = []
    let k = 0
    while (k < fruits.length) {
      if (k + 1 < fruits.length && fruits[k] === fruits[k + 1]) {
        fusionnes.push(fruits[k] + 1)
        pointsGagnes += (fruits[k] + 1) * 10
        k += 2
      } else {
        fusionnes.push(fruits[k])
        k += 1
      }
    }
    while (fusionnes.length < taille.value) fusionnes.push(null)
    indices.forEach((indexGrille, positionLigne) => {
      if (grille.value[indexGrille] !== fusionnes[positionLigne]) aBouge = true
      grille.value[indexGrille] = fusionnes[positionLigne]
    })
  }
  return { aBouge, pointsGagnes }
}

function unCoupRestant() {
  const n = taille.value
  for (let i = 0; i < n * n; i += 1) {
    if (grille.value[i] === null) return true
    const colonne = i % n
    const ligne = Math.floor(i / n)
    if (colonne + 1 < n && grille.value[i] === grille.value[i + 1]) return true
    if (ligne + 1 < n && grille.value[i] === grille.value[i + n]) return true
  }
  return false
}

function jouerCoup(direction) {
  if (etape.value !== 'jeu') return
  const resultat = deplacer(direction)
  if (!resultat.aBouge) return
  score.value += resultat.pointsGagnes
  spawn()
  meilleurFruit.value = Math.max(...grille.value.filter((v) => v !== null), meilleurFruit.value)
  if (grille.value.includes(INDEX_PASTEQUE)) {
    terminer(true)
  } else if (!unCoupRestant()) {
    terminer(false)
  }
}

/* --- Toucher (glisser) --------------------------------------------------- */
let positionToucher = null
function debutToucher(evenement) {
  positionToucher = { x: evenement.touches[0].clientX, y: evenement.touches[0].clientY }
}
function finToucher(evenement) {
  if (!positionToucher || etape.value !== 'jeu') return
  const dx = evenement.changedTouches[0].clientX - positionToucher.x
  const dy = evenement.changedTouches[0].clientY - positionToucher.y
  positionToucher = null
  if (Math.abs(dx) < 24 && Math.abs(dy) < 24) return
  if (Math.abs(dx) > Math.abs(dy)) jouerCoup(dx > 0 ? 'droite' : 'gauche')
  else jouerCoup(dy > 0 ? 'bas' : 'haut')
}

/* --- Clavier ------------------------------------------------------------- */
function toucheClavier(evenement) {
  const correspondances = {
    ArrowLeft: 'gauche',
    ArrowRight: 'droite',
    ArrowUp: 'haut',
    ArrowDown: 'bas',
  }
  if (correspondances[evenement.key]) {
    evenement.preventDefault()
    jouerCoup(correspondances[evenement.key])
  }
}
onMounted(() => window.addEventListener('keydown', toucheClavier))
onUnmounted(() => window.removeEventListener('keydown', toucheClavier))

/* --- Fin de partie -------------------------------------------------------- */
function terminer(victoire) {
  gagne.value = victoire
  const nbEtoiles = victoire ? 3 : 1
  noterScore('fruits', progression.niveau, score.value, nbEtoiles)
  API.envoyerScore({
    pseudo: progression.pseudo,
    jeu: 'fruits',
    niveau: progression.niveau,
    points: score.value,
    etoiles: nbEtoiles,
  })
  etape.value = 'fin'
}

watch(() => progression.niveau, () => {
  if (etape.value !== 'fin') etape.value = 'accueil'
})
</script>

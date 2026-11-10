<template>
  <section class="mx-auto max-w-xl">
    <div class="mb-4 flex items-center justify-between gap-3">
      <RouterLink
        to="/"
        class="rounded-full bg-white px-4 py-2 text-sm font-extrabold text-[#6d28d9] shadow-sm transition-shadow hover:shadow-md"
      >
        ← Accueil
      </RouterLink>
      <h1 class="text-2xl font-extrabold text-[#6d28d9]">Sudoku</h1>
      <span class="text-sm font-bold text-amber-700">⭐ {{ progression.etoiles }}</span>
    </div>

    <div class="rounded-3xl bg-white p-5 shadow-sm sm:p-7">
      <p class="mb-4 text-center text-[0.95rem] font-bold text-[#3f3556]">
        Chaque ligne, chaque colonne et chaque bloc de 4 doit contenir les chiffres 1, 2, 3 et 4.
      </p>

      <!-- Grille -->
      <div class="mx-auto grid w-fit grid-cols-4 gap-1 rounded-2xl border-4 border-[#8fd3a8] bg-[#eef8f0] p-2">
        <button
          v-for="(cellule, index) in grillePlat"
          :key="index"
          class="flex h-14 w-14 items-center justify-center rounded-lg text-[1.3rem] font-extrabold transition-colors sm:h-16 sm:w-16"
          :class="
            cellule.fixe
              ? 'bg-[#d8f3dc] text-[#14532d]'
              : selection === index
                ? 'bg-[#bbf7d0] text-[#166534] ring-2 ring-[#22c55e]'
                : 'bg-white text-[#15803d] hover:bg-[#f0fdf4]'
          "
          @click="choisir(index)"
        >
          {{ cellule.valeur || '' }}
        </button>
      </div>

      <!-- Chiffres -->
      <div class="mx-auto mt-5 flex w-fit justify-center gap-2.5">
        <button
          v-for="n in 4"
          :key="n"
          class="h-12 w-12 rounded-full bg-[#dcf3e3] text-[1.15rem] font-extrabold text-[#166534] transition-transform hover:scale-110"
          @click="placer(n)"
        >
          {{ n }}
        </button>
        <button
          class="h-12 w-12 rounded-full bg-slate-100 text-lg font-extrabold text-slate-500 transition-transform hover:scale-110"
          @click="placer(0)"
          title="Effacer"
        >
          ✕
        </button>
      </div>

      <p v-if="message" class="mt-4 text-center text-[1rem] font-bold" :class="gagne ? 'text-green-600' : 'text-amber-600'">
        {{ message }}
      </p>

      <div class="mt-5 flex justify-center gap-3">
        <button
          class="rounded-full bg-[#6d28d9] px-8 py-3 font-extrabold text-white transition-transform hover:scale-105"
          @click="nouvelleGrille"
        >
          Nouvelle grille
        </button>
        <button
          v-if="!gagne"
          class="rounded-full bg-[#dcf3e3] px-6 py-3 font-extrabold text-[#166534] transition-transform hover:scale-105"
          @click="verifier"
        >
          Vérifier
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { RouterLink } from 'vue-router'
import { progression, noterScore } from '../stores/progression'

/* Grille 4x4 jouée comme un tableau plat de {valeur, fixe}. */
const grillePlat = ref([])
const selection = ref(-1)
const message = ref('')
const gagne = ref(false)
const fautes = ref(0)

function melange(liste) {
  for (let i = liste.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[liste[i], liste[j]] = [liste[j], liste[i]]
  }
  return liste
}

/* Base valide, chiffres mélangés + permutation de lignes dans leurs blocs. */
function generer() {
  const chiffres = melange([1, 2, 3, 4])
  const lignes = [
    [chiffres[0], chiffres[1], chiffres[2], chiffres[3]],
    [chiffres[2], chiffres[3], chiffres[0], chiffres[1]],
    [chiffres[1], chiffres[0], chiffres[3], chiffres[2]],
    [chiffres[3], chiffres[2], chiffres[1], chiffres[0]],
  ]
  return lignes
}

function nouvelleGrille() {
  const pleine = generer()
  const solution = pleine.flat()
  const casesCachees = new Set()
  while (casesCachees.size < 7) casesCachees.add(Math.floor(Math.random() * 16))

  grillePlat.value = solution.map((valeur, index) => ({
    valeur: casesCachees.has(index) ? 0 : valeur,
    fixe: !casesCachees.has(index),
    solution,
  }))
  selection.value = -1
  message.value = ''
  gagne.value = false
  fautes.value = 0
}

function choisir(index) {
  if (grillePlat.value[index].fixe || gagne.value) return
  if (grillePlat.value[index].valeur !== 0) {
    grillePlat.value[index].valeur = 0
    return
  }
  selection.value = index
}

function placer(n) {
  const index = selection.value
  if (index < 0 || gagne.value) return
  grillePlat.value[index].valeur = n
  selection.value = -1
  if (!grillePlat.value.some((c) => c.valeur === 0)) verifier()
}

function valider() {
  const g = grillePlat.value
  const lignesOk = [0, 1, 2, 3].every((l) =>
    new Set([0, 1, 2, 3].map((c) => g[l * 4 + c].valeur)).size === 4,
  )
  const colonnesOk = [0, 1, 2, 3].every((c) =>
    new Set([0, 1, 2, 3].map((l) => g[l * 4 + c].valeur)).size === 4,
  )
  const blocsOk = [0, 1, 2, 3].every((b) => {
    const l0 = Math.floor(b / 2) * 2
    const c0 = (b % 2) * 2
    return new Set([
      g[l0 * 4 + c0].valeur,
      g[l0 * 4 + c0 + 1].valeur,
      g[(l0 + 1) * 4 + c0].valeur,
      g[(l0 + 1) * 4 + c0 + 1].valeur,
    ]).size === 4
  })
  return lignesOk && colonnesOk && blocsOk
}

function verifier() {
  if (valider()) {
    gagne.value = true
    message.value = 'Bravo, la grille est parfaite ! 🎉'
    const etoiles = fautes.value === 0 ? 3 : fautes.value <= 2 ? 2 : 1
    noterScore('sudoku', progression.niveau, etoiles * 10 + 20, etoiles)
  } else {
    fautes.value += 1
    message.value = 'Presque ! Vérifie tes lignes, colonnes et blocs.'
  }
}

onMounted(nouvelleGrille)
</script>

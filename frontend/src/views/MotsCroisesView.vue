<template>
  <section class="mx-auto max-w-xl">
    <div class="mb-4 flex items-center justify-between gap-3">
      <RouterLink
        to="/"
        class="rounded-full bg-white px-4 py-2 text-sm font-extrabold text-[#6d28d9] shadow-sm transition-shadow hover:shadow-md"
      >
        ← Accueil
      </RouterLink>
      <h1 class="text-2xl font-extrabold text-[#6d28d9]">Mots croisés</h1>
      <span class="text-sm font-bold text-amber-700">⭐ {{ progression.etoiles }}</span>
    </div>

    <div class="rounded-3xl bg-white p-5 shadow-sm sm:p-7">
      <!-- Grille -->
      <div class="mx-auto w-fit">
        <div v-for="(rangée, r) in grille" :key="r" class="flex gap-1">
          <template v-for="(cellule, c) in rangée" :key="r + '-' + c">
            <div v-if="cellule" class="relative">
              <input
                :ref="mot(r, c)"
                class="h-11 w-11 rounded-md border-2 text-center text-[1.05rem] font-extrabold uppercase outline-none transition-colors"
                :class="
                  etats[r + '-' + c] === 'ok'
                    ? 'border-green-500 bg-green-50 text-green-700'
                    : etats[r + '-' + c] === 'faux'
                      ? 'border-rose-400 bg-rose-50 text-rose-600'
                      : 'border-[#e8d48a] bg-white text-[#a16207] focus:border-[#6d28d9]'
                "
                maxlength="1"
                :value="reponses[r + '-' + c] || ''"
                aria-label="Lettre"
                @input="ecrire(r, c, $event)"
              />
              <span
                v-if="cellule.num"
                class="pointer-events-none absolute left-1 top-0.5 text-[0.6rem] font-extrabold text-slate-400"
              >{{ cellule.num }}</span>
            </div>
            <div v-else class="h-11 w-11 rounded-md bg-slate-800"></div>
          </template>
        </div>
      </div>

      <!-- Indices -->
      <div class="mt-5 grid gap-3 sm:grid-cols-2">
        <div class="rounded-2xl bg-[#fdf8e7] p-4">
          <p class="mb-2 font-extrabold text-[#a16207]">Ligne ➡️</p>
          <p class="text-[0.9rem] font-semibold text-slate-700">
            <b>1.</b> Il aboie et remue la queue (5)<br />
            <b>3.</b> Article : « ___ fleur » (3)<br />
            <b>4.</b> Les arbres donnent du... (4)
          </p>
        </div>
        <div class="rounded-2xl bg-[#f3f0ff] p-4">
          <p class="mb-2 font-extrabold text-[#6d28d9]">Colonne ⬇️</p>
          <p class="text-[0.9rem] font-semibold text-slate-700">
            <b>1.</b> Il a 4 côtés égaux (4)<br />
            <b>2.</b> Tu sens avec (3)
          </p>
        </div>
      </div>

      <p v-if="message" class="mt-4 text-center text-[1rem] font-bold" :class="gagne ? 'text-green-600' : 'text-amber-600'">
        {{ message }}
      </p>

      <div class="mt-5 flex justify-center gap-3">
        <button
          class="rounded-full bg-[#6d28d9] px-8 py-3 font-extrabold text-white transition-transform hover:scale-105"
          @click="verifier"
        >
          Vérifier
        </button>
        <button
          class="rounded-full bg-[#fdf3c9] px-6 py-3 font-extrabold text-amber-800 transition-transform hover:scale-105"
          @click="aide"
        >
          Indice 💡
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { RouterLink } from 'vue-router'
import { progression, noterScore } from '../stores/progression'

/* Grille : null = case noire ; sol = lettre attendue ; num = numéro de mot. */
const grille = [
  [{ sol: 'C', num: 1 }, { sol: 'H' }, { sol: 'I' }, { sol: 'E' }, { sol: 'N', num: 2 }],
  [{ sol: 'U', num: 3 }, { sol: 'N' }, { sol: 'E' }, null, { sol: 'E' }],
  [{ sol: 'B', num: 4 }, { sol: 'O' }, { sol: 'I' }, { sol: 'S' }, { sol: 'Z' }],
  [{ sol: 'E' }, null, null, null, null],
]

const reponses = reactive({})
const etats = reactive({})
const message = ref('')
const gagne = ref(false)
const indicesUtilises = ref(0)
const refsLettres = {}

function mot(r, c) {
  return (el) => {
    if (el) refsLettres[`${r}-${c}`] = el
  }
}

function ecrire(r, c, evenement) {
  const cible = evenement.target
  const lettre = (cible.value || '').toUpperCase().slice(-1)
  cible.value = lettre
  reponses[`${r}-${c}`] = lettre
  etats[`${r}-${c}`] = ''

  // petite commodité : on passe à la case suivante de la ligne
  if (lettre && c + 1 < 5 && grille[r][c + 1]) {
    const suivant = refsLettres[`${r}-${c + 1}`]
    if (suivant) suivant.focus()
  }
}

function verifier() {
  let correctes = 0
  let totales = 0
  for (const [r, rangée] of grille.entries()) {
    for (const [c, cellule] of rangée.entries()) {
      if (!cellule) continue
      totales += 1
      const reponse = (reponses[`${r}-${c}`] || '').toUpperCase()
      if (reponse === cellule.sol) {
        etats[`${r}-${c}`] = 'ok'
        correctes += 1
      } else if (reponse) {
        etats[`${r}-${c}`] = 'faux'
      } else {
        etats[`${r}-${c}`] = ''
      }
    }
  }
  if (correctes === totales) {
    gagne.value = true
    message.value = 'Bravo, tous les mots sont trouvés ! 🎉'
    const etoiles = indicesUtilises.value === 0 ? 3 : 2
    noterScore('mots', progression.niveau, correctes * 4 + 20, etoiles)
  } else {
    message.value = `Trouvé ${correctes} lettres sur ${totales}. Continue !`
  }
}

function aide() {
  for (const [r, rangée] of grille.entries()) {
    for (const [c, cellule] of rangée.entries()) {
      if (!cellule) continue
      const reponse = (reponses[`${r}-${c}`] || '').toUpperCase()
      if (reponse !== cellule.sol) {
        reponses[`${r}-${c}`] = cellule.sol
        etats[`${r}-${c}`] = 'ok'
        indicesUtilises.value += 1
        return
      }
    }
  }
  verifier()
}
</script>

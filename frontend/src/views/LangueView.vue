<template>
  <section class="mx-auto max-w-2xl">
    <div class="mb-4 flex items-center justify-between gap-3">
      <RouterLink
        to="/"
        class="rounded-full bg-white px-4 py-2 text-sm font-extrabold text-[#6d28d9] shadow-sm transition-shadow hover:shadow-md"
      >
        ← Accueil
      </RouterLink>
      <h1 class="text-2xl font-extrabold text-[#6d28d9]">Langue</h1>
      <span class="text-sm font-bold text-amber-700">⭐ {{ progression.etoiles }}</span>
    </div>

    <div class="rounded-3xl bg-white p-5 shadow-sm sm:p-7">
      <!-- Accueil -->
      <div v-if="etape === 'accueil'" class="py-3 text-center">
        <p class="text-[1.1rem] font-extrabold text-[#3f3556]">Le français et l'anglais 🇫🇷🇬🇧</p>
        <p class="mx-auto mb-5 mt-1 max-w-sm text-[0.9rem] font-medium text-slate-500">
          Milo te montre un mot avec son dessin : trouve sa traduction !
        </p>
        <button
          class="rounded-full bg-[#6d28d9] px-8 py-3 font-extrabold text-white transition-transform hover:scale-105"
          @click="lancer"
        >
          C'est parti !
        </button>
      </div>

      <!-- Jeu -->
      <div v-else-if="etape === 'jeu'">
        <div class="mb-4 flex flex-wrap items-center justify-center gap-3">
          <p class="rounded-full bg-[#f3f0ff] px-4 py-2 text-sm font-extrabold text-[#6d28d9]">
            Mot {{ numero + 1 }} sur {{ questionSet.length }}
          </p>
          <p class="rounded-full bg-[#fdf3c9] px-4 py-2 text-sm font-extrabold text-amber-800">
            ⭐ {{ points }} pts
          </p>
        </div>

        <div v-if="questionCourante" class="mx-auto max-w-sm rounded-3xl bg-[#f7f4fe] p-5 text-center">
          <p class="text-[2.6rem] leading-none">{{ questionCourante.emoji }}</p>
          <p class="mt-2 text-[1.35rem] font-extrabold text-[#2d2a45]">
            {{ questionCourante.mot }}
          </p>
          <p class="mt-0.5 text-[0.85rem] font-bold text-slate-500">
            {{ questionCourante.direction === 'fr-en' ? 'En anglais ?' : 'En français ?' }}
          </p>
        </div>

        <div class="mx-auto mt-4 flex max-w-sm flex-col gap-2.5">
          <button
            v-for="(choix, i) in questionCourante?.choix ?? []"
            :key="i"
            class="rounded-full py-3 text-[1rem] font-extrabold transition-colors"
            :class="
              dejaRepondu && choix !== questionCourante.reponse
                ? 'bg-[#f5f3fb] text-slate-400'
                : dejaRepondu && choix === questionCourante.reponse
                  ? 'bg-green-500 text-white'
                  : 'bg-[#f3f0ff] text-[#6d28d9] hover:bg-[#ebe4fc]'
            "
            :disabled="dejaRepondu"
            @click="repondre(choix)"
          >
            {{ choix }}
          </button>
        </div>

        <p v-if="message" class="mt-4 text-center text-[1rem] font-bold" :class="derniere ? 'text-green-600' : 'text-rose-500'">
          {{ message }}
        </p>
      </div>

      <!-- Fin -->
      <div v-else class="py-3 text-center">
        <p class="text-5xl">{{ correctes >= 7 ? '🏆' : correctes >= 4 ? '🌟' : '💪' }}</p>
        <p class="mt-2 text-xl font-extrabold text-[#2d2a45]">{{ correctes }} mots réussis !</p>
        <p class="mt-1 font-bold text-slate-500">Score : {{ points }} points</p>
        <div class="mt-4 flex justify-center gap-3">
          <button
            class="rounded-full bg-[#6d28d9] px-8 py-3 font-extrabold text-white transition-transform hover:scale-105"
            @click="lancer"
          >
            Rejouer
          </button>
          <RouterLink
            to="/"
            class="rounded-full bg-[#f3f0ff] px-8 py-3 font-extrabold text-[#6d28d9] transition-colors hover:bg-[#ebe4fc]"
          >
            Maison
          </RouterLink>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, ref } from 'vue'
import { RouterLink } from 'vue-router'
import { progression, noterScore } from '../stores/progression'

const MOTS = [
  { emoji: '🐱', fr: 'chat', en: 'cat' },
  { emoji: '🐶', fr: 'chien', en: 'dog' },
  { emoji: '☀️', fr: 'soleil', en: 'sun' },
  { emoji: '🌙', fr: 'lune', en: 'moon' },
  { emoji: '🏠', fr: 'maison', en: 'house' },
  { emoji: '🍎', fr: 'pomme', en: 'apple' },
  { emoji: '🐟', fr: 'poisson', en: 'fish' },
  { emoji: '⭐', fr: 'étoile', en: 'star' },
  { emoji: '🤝', fr: 'ami', en: 'friend' },
  { emoji: '🎒', fr: 'école', en: 'school' },
  { emoji: '🥕', fr: 'carotte', en: 'carrot' },
  { emoji: '🐦', fr: 'oiseau', en: 'bird' },
]

const etape = ref('accueil')
const questionSet = ref([])
const numero = ref(0)
const points = ref(0)
const correctes = ref(0)
const dejaRepondu = ref(false)
const message = ref('')
const derniere = ref(false)

const questionCourante = computed(() => questionSet.value[numero.value] ?? null)

function lancer() {
  const tirage = [...MOTS].sort(() => Math.random() - 0.5).slice(0, 8)
  questionSet.value = tirage.map((m) => {
    const direction = Math.random() < 0.5 ? 'fr-en' : 'en-fr'
    const mot = direction === 'fr-en' ? m.fr : m.en
    const reponse = direction === 'fr-en' ? m.en : m.fr
    const distracteurs = [...MOTS]
      .filter((x) => x !== m)
      .sort(() => Math.random() - 0.5)
      .slice(0, 2)
      .map((x) => (direction === 'fr-en' ? x.en : x.fr))
    const choix = [reponse, ...distracteurs].sort(() => Math.random() - 0.5)
    return { ...m, mot, reponse, direction, choix }
  })
  numero.value = 0
  points.value = 0
  correctes.value = 0
  dejaRepondu.value = false
  message.value = ''
  etape.value = 'jeu'
}

function repondre(choix) {
  if (dejaRepondu.value) return
  dejaRepondu.value = true
  const bonne = choix === questionCourante.value.reponse
  if (bonne) {
    points.value += 15
    correctes.value += 1
    derniere.value = true
    message.value = 'Bravo ! Correct !'
  } else {
    derniere.value = false
    message.value = `Presque : on disait « ${questionCourante.value.reponse} »`
  }
  setTimeout(suivant, 1100)
}

function suivant() {
  message.value = ''
  dejaRepondu.value = false
  if (numero.value + 1 < questionSet.value.length) {
    numero.value += 1
  } else {
    finir()
  }
}

function finir() {
  const etoiles = correctes.value >= 7 ? 3 : correctes.value >= 4 ? 2 : correctes.value >= 2 ? 1 : 0
  if (points.value > 0) {
    noterScore('langue', progression.niveau, points.value, etoiles)
  }
  etape.value = 'fin'
}
</script>

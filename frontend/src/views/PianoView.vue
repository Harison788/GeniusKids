<template>
  <section class="mx-auto max-w-2xl">
    <div class="mb-4 flex items-center justify-between gap-3">
      <RouterLink
        to="/"
        class="rounded-full bg-white px-4 py-2 text-sm font-extrabold text-[#6d28d9] shadow-sm transition-shadow hover:shadow-md"
      >
        ← Accueil
      </RouterLink>
      <h1 class="text-2xl font-extrabold text-[#6d28d9]">Piano</h1>
      <span class="text-sm font-bold text-amber-700">⭐ {{ progression.etoiles }}</span>
    </div>

    <div class="rounded-3xl bg-white p-5 shadow-sm sm:p-7">
      <!-- Accueil -->
      <div v-if="etape === 'accueil'" class="mb-6 text-center">
        <p class="text-[1.05rem] font-bold text-[#3f3556]">
          Appuie sur les touches pour jouer...
        </p>
        <p class="mb-4 text-[0.9rem] font-medium text-slate-500">
          ou lance « Répète la mélodie » : Milo joue, à toi de le refaire !
        </p>
        <button
          class="rounded-full bg-[#6d28d9] px-8 py-3 text-[1rem] font-extrabold text-white transition-transform hover:scale-105"
          @click="lancerJeu"
        >
          Répète la mélodie
        </button>
      </div>

      <!-- Jeu : répète la mélodie -->
      <div v-else-if="etape === 'jeu'" class="mb-6 text-center">
        <div class="mb-3 flex flex-wrap items-center justify-center gap-3">
          <p class="rounded-full bg-[#f3f0ff] px-4 py-2 text-sm font-extrabold text-[#6d28d9]">
            Mélodie {{ manche }} sur 6
          </p>
          <p class="rounded-full bg-[#fdf3c9] px-4 py-2 text-sm font-extrabold text-amber-800">
            ⭐ {{ points }} pts
          </p>
        </div>
        <p class="text-[1rem] font-bold text-[#3f3556]">
          {{ aTonTour ? 'À toi de rejouer la mélodie !' : 'Milo joue... écoute bien 👂' }}
        </p>
        <p v-if="message" class="mt-2 text-[0.95rem] font-bold" :class="reussi ? 'text-green-600' : 'text-rose-500'">
          {{ message }}
        </p>
      </div>

      <!-- Fin -->
      <div v-else class="mb-6 text-center">
        <p class="text-5xl">{{ manchesGagnees >= 4 ? '🌟🌟' : manchesGagnees >= 2 ? '🌟' : '🎹' }}</p>
        <p class="mt-2 text-xl font-extrabold text-[#2d2a45]">{{ manchesGagnees }} mélodies réussies !</p>
        <p class="mt-1 font-bold text-slate-500">Score : {{ points }} points</p>
        <div class="mt-4 flex justify-center gap-3">
          <button
            class="rounded-full bg-[#6d28d9] px-8 py-3 font-extrabold text-white transition-transform hover:scale-105"
            @click="lancerJeu"
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

      <!-- Le clavier (toujours affiché) -->
      <div class="clavier">
        <div class="relative flex w-full gap-1.5">
          <button
            v-for="(touche, i) in TOUCHES"
            :key="i"
            class="touche-blanche"
            :class="{ eclairee: toucheEclairee === i, jouable: aTonTour }"
            :style="touche.haut ? 'font-size:0.9rem' : ''"
            @pointerdown="presser(i)"
          >
            {{ touche.nom }}
          </button>

          <!-- touches noires -->
          <span
            v-for="noir in NOIRS"
            :key="'n' + noir.apres"
            class="noire"
            :style="{ left: `calc(${(noir.apres + 1) * 12.5 - 3.4}% - 6px)` }"
          ></span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { progression, noterScore } from '../stores/progression'

/* Touches blanches d'une octave + emplacements des touches noires (déco). */
const TOUCHES = [
  { nom: 'Do', freq: 261.63 },
  { nom: 'Ré', freq: 293.66 },
  { nom: 'Mi', freq: 329.63 },
  { nom: 'Fa', freq: 349.23 },
  { nom: 'Sol', freq: 392.0 },
  { nom: 'La', freq: 440.0 },
  { nom: 'Si', freq: 493.88 },
  { nom: 'Do', nom2: 'octave', freq: 523.25 },
]
const NOIRS = [
  { apres: 0 },
  { apres: 1 },
  { apres: 3 },
  { apres: 4 },
  { apres: 5 },
]

let ctx = null
function jouer(freq) {
  try {
    ctx = ctx || new (window.AudioContext || window.webkitAudioContext)()
    const osc = ctx.createOscillator()
    const gain = ctx.createGain()
    osc.type = 'triangle'
    osc.frequency.value = freq
    gain.gain.setValueAtTime(0.35, ctx.currentTime)
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.7)
    osc.connect(gain).connect(ctx.destination)
    osc.start()
    osc.stop(ctx.currentTime + 0.7)
  } catch {
    // L'audio démarre après le premier clic : pas bloquant.
  }
}

const etape = ref('accueil')
const manche = ref(1)
const manchesGagnees = ref(0)
const points = ref(0)
const message = ref('')
const reussi = ref(false)
const melodie = ref([])
const joues = ref([])
const aTonTour = ref(false)
const toucheEclairee = ref(-1)

/* Libre : on fait juste sonner la touche. */
function presser(i) {
  jouer(TOUCHES[i].freq)
  clignote(i)
  if (etape.value === 'jeu' && aTonTour.value && !message.value.includes('presque')) {
    verifier(i)
  }
}

function clignote(i) {
  toucheEclairee.value = i
  setTimeout(() => { if (toucheEclairee.value === i) toucheEclairee.value = -1 }, 180)
}

function lancerJeu() {
  etape.value = 'jeu'
  manche.value = 1
  manchesGagnees.value = 0
  points.value = 0
  message.value = ''
  aTonTour.value = false
  setTimeout(jouerManche, 500)
}

/* Génère et joue la mélodie du tour courant. */
function jouerManche() {
  const longueur = manche.value
  melodie.value = Array.from({ length: longueur }, () => Math.floor(Math.random() * 8))
  joues.value = []
  aTonTour.value = false
  message.value = ''

  melodie.value.forEach((indice, position) => {
    setTimeout(() => {
      jouer(TOUCHES[indice].freq)
      clignote(indice)
    }, position * 650)
  })
  setTimeout(() => {
    aTonTour.value = true
  }, melodie.value.length * 650 + 300)
}

function verifier(i) {
  const attendu = melodie.value[joues.value.length]
  if (i !== attendu) {
    aTonTour.value = false
    message.value = `Presque ! Terminé : ${manchesGagnees.value} mélodies.`
    reussi.value = false
    finir()
    return
  }
  joues.value.push(i)
  if (joues.value.length === melodie.value.length) {
    manchesGagnees.value += 1
    points.value += manche.value * 20
    reussi.value = true
    message.value = 'Super !'
    if (manche.value === 6) {
      aTonTour.value = false
      setTimeout(finir, 900)
    } else {
      manche.value += 1
      aTonTour.value = false
      setTimeout(jouerManche, 900)
    }
  }
}

function finir() {
  const etoiles = manchesGagnees.value >= 5 ? 3 : manchesGagnees.value >= 3 ? 2 : manchesGagnees.value >= 1 ? 1 : 0
  if (points.value > 0) {
    noterScore('piano', progression.niveau, points.value, etoiles)
  }
  etape.value = 'fin'
}
</script>

<style scoped>
.clavier {
  background: #4c3a8f;
  padding: 14px;
  border-radius: 18px;
}
.touche-blanche {
  position: relative;
  z-index: 1;
  flex: 1;
  height: 130px;
  border-radius: 0 0 10px 10px;
  background: #ffffff;
  font-weight: 800;
  color: #6d28d9;
  transition: background 0.08s, transform 0.08s;
}
.touche-blanche.jouable {
  cursor: pointer;
  box-shadow: inset 0 -6px 0 #ede9fe;
}
.touche-blanche.eclairee {
  background: #fde68a;
  transform: scale(0.97);
}
.noire {
  position: absolute;
  top: 0;
  z-index: 2;
  width: 7%;
  height: 62%;
  background: #2e2a5e;
  border-radius: 0 0 5px 5px;
  margin-left: -3.5%;
  pointer-events: none;
}
</style>

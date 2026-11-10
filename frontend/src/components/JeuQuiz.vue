<template>
  <section class="jeu">
    <h1 class="titre-jeu">{{ titre }}</h1>

    <p v-if="erreur" class="message-erreur">
      {{ erreur }}<br />
      <button class="btn-gros" @click="demarrer">Réessayer</button>
    </p>

    <template v-if="etape === 'accueil'">
      <p class="rappel-niveau">Rends-toi à l'accueil pour changer de niveau.</p>
      <button class="btn-gros" @click="demarrer">C'est parti !</button>
    </template>

    <template v-else-if="etape === 'jeu'">
      <div class="barre-progression">
        <div class="barre-progression-interne" :style="{ width: avancement + '%' }"></div>
      </div>
      <p class="compteur">Question {{ numero + 1 }} / {{ questions.length }} • ⭐ {{ points }} pts</p>

      <div v-if="questionCourante" class="carte-question">
        <p v-if="questionCourante.affichage" class="affichage">{{ questionCourante.affichage }}</p>
        <p class="question">{{ questionCourante.question }}</p>
      </div>

      <div class="grille-choix">
        <button
          v-for="(choix, i) in questionCourante?.choix ?? []"
          :key="i"
          class="btn-choix"
          :disabled="dejaRepondu"
          @click="repondre(choix)"
        >
          {{ choix }}
        </button>
      </div>

      <p class="message-feedback" :class="{ positif: derniereReussie }" v-if="message">{{ message }}</p>
    </template>

    <template v-else-if="etape === 'fin'">
      <div class="carte-gagnant">
        <p class="etoiles-grandes">
          {{ '⭐'.repeat(etoiles) + '☆'.repeat(3 - etoiles) }}
        </p>
        <p class="score-final">Score : {{ points }} points</p>
        <p class="bravo">Super travail, champion ! 🎉</p>
      </div>
      <div class="rangee-boutons">
        <button class="btn-gros" @click="demarrer">Rejouer</button>
        <RouterLink to="/" class="btn-lien">Maison</RouterLink>
      </div>
    </template>
  </section>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { RouterLink } from 'vue-router'
import API from '../api'
import { progression, noterScore } from '../stores/progression'

const props = defineProps({
  jeu: { type: String, required: true },
  titre: { type: String, required: true },
  emoji: { type: String, default: '🎮' },
})

const NIVEAUX = { 1: 'Écureuil 🐿️', 2: 'Renard 🦊', 3: 'Hibou 🦉' }

const etape = ref('accueil')
const erreur = ref('')
const questions = ref([])
const numero = ref(0)
const points = ref(0)
const message = ref('')
const dejaRepondu = ref(false)
const etoiles = ref(0)
const derniereReussie = ref(false)

const niveau = computed(() => `${NIVEAUX[progression.niveau] ?? ''}`)
const questionCourante = computed(() => questions.value[numero.value] ?? null)
const avancement = computed(() =>
  questions.value.length ? Math.round((numero.value / questions.value.length) * 100) : 0
)

async function demarrer() {
  erreur.value = ''
  message.value = ''
  etoiles.value = 0
  etape.value = 'chargement'
  try {
    const donnees = await API.charger(props.jeu, progression.niveau)
    questions.value = donnees.questions
    numero.value = 0
    points.value = 0
    etape.value = 'jeu'
  } catch {
    erreur.value = 'Oups, impossible de lancer le jeu. Le serveur tourne-t-il ?'
    etape.value = 'accueil'
  }
}

function repondre(choix) {
  if (dejaRepondu.value || !questionCourante.value) return
  dejaRepondu.value = true
  const bonne = Number(questionCourante.value.reponse)
  if (Number(choix) === bonne) {
    points.value += 10
    derniereReussie.value = true
    message.value = 'Bravo, c\'est gagné !'
  } else {
    derniereReussie.value = false
    message.value = `Presque ! La bonne réponse était ${bonne}`
  }
  setTimeout(continuer, 1200)
}

function continuer() {
  message.value = ''
  dejaRepondu.value = false
  if (numero.value + 1 < questions.value.length) {
    numero.value += 1
  } else {
    terminer()
  }
}

function terminer() {
  const ratio = points.value / (questions.value.length * 10)
  etoiles.value = ratio >= 0.9 ? 3 : ratio >= 0.6 ? 2 : 1
  noterScore(props.jeu, progression.niveau, points.value, etoiles.value)
  API.envoyerScore({
    pseudo: progression.pseudo,
    jeu: props.jeu,
    niveau: progression.niveau,
    points: points.value,
    etoiles: etoiles.value,
  })
  etape.value = 'fin'
}

// Si le niveau change dans un autre onglet, on revient à l'accueil du jeu.
watch(() => progression.niveau, () => {
  if (etape.value !== 'fin') etape.value = 'accueil'
})
</script>

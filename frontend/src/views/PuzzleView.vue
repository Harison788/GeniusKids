<template>
  <section class="jeu">
    <h1 class="titre-jeu">Puzzle</h1>

    <p v-if="erreur" class="message-erreur">
      {{ erreur }}<br />
      <button class="btn-gros" @click="demarrer">Réessayer</button>
    </p>

    <template v-if="etape === 'accueil'">
      <p class="rappel-niveau">
        Le dessin est mélangé : touche deux pièces pour les échanger et remets tout à sa place.
      </p>
      <button class="btn-gros" @click="demarrer">C'est parti !</button>
    </template>

    <template v-else-if="etape === 'jeu'">
      <p class="compteur">Échanges : {{ coups }}</p>

      <div class="pieces-puzzle" :style="{ '--colonnes-puzzle': taille }">
        <button
          v-for="(piece, index) in pieces"
          :key="index"
          class="piece-puzzle"
          :class="{ 'est-choisie': index === choix }"
          :style="stylePiece(piece)"
          :aria-label="'Pièce ' + (piece + 1)"
          @click="choisirPiece(index)"
        ></button>
      </div>
      <p class="message-feedback" v-if="message">{{ message }}</p>
    </template>

    <template v-else-if="etape === 'fin'">
      <div class="carte-gagnant">
        <p class="etoiles-grandes">{{ '★'.repeat(etoiles) + '☆'.repeat(3 - etoiles) }}</p>
        <p class="score-final">Score : {{ points }} points</p>
        <div class="image-terminee" :style="styleImageComplete"></div>
        <p class="bravo">Le puzzle est terminé en {{ coups }} échanges !</p>
      </div>
      <div class="rangee-boutons">
        <button class="btn-gros" @click="demarrer">Rejouer</button>
        <RouterLink to="/" class="btn-lien">Maison</RouterLink>
      </div>
    </template>
  </section>
</template>

<script setup>
import { ref, watch } from 'vue'
import { RouterLink } from 'vue-router'
import API from '../api'
import { progression, noterScore } from '../stores/progression'

/* Le dessin à reconstituer : une petite scène colorée (SVG incorporé). */
const SVG_SCENE = `
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 120'>
  <rect width='120' height='120' fill='#aee3f5'/>
  <circle cx='98' cy='22' r='13' fill='#ffb703'/>
  <ellipse cx='32' cy='26' rx='17' ry='8' fill='#ffffff'/>
  <ellipse cx='45' cy='21' rx='11' ry='6' fill='#ffffff'/>
  <rect y='80' width='120' height='40' fill='#7fbf30'/>
  <rect x='58' y='52' width='36' height='32' fill='#fb8500'/>
  <polygon points='52,52 76,32 102,52' fill='#ef476f'/>
  <rect x='70' y='64' width='10' height='13' fill='#fff8ec'/>
  <rect x='24' y='60' width='9' height='24' fill='#8d5524'/>
  <circle cx='28' cy='50' r='15' fill='#2a9d8f'/>
  <circle cx='98' cy='94' r='5' fill='#ef476f'/>
  <circle cx='12' cy='96' r='5' fill='#ffb703'/>
  <rect x='37' y='74' width='70' height='0.01'/>
</svg>`

const IMAGE_URI = 'data:image/svg+xml;utf8,' + encodeURIComponent(SVG_SCENE)

const etape = ref('accueil')
const erreur = ref('')
const taille = ref(3)
const pieces = ref([])
const choix = ref(null)
const coups = ref(0)
const message = ref('')
const etoiles = ref(0)
const points = ref(0)

function melanger(nomb) {
  const ordre = Array.from({ length: nomb }, (_, i) => i)
  let melangeOK = false
  while (!melangeOK) {
    for (let i = nomb - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[ordre[i], ordre[j]] = [ordre[j], ordre[i]]
    }
    // On force au moins un désordre, sinon la partie serait déjà finie.
    melangeOK = ordre.some((v, i) => v !== i)
  }
  return ordre
}

function demarrer() {
  erreur.value = ''
  taille.value = progression.niveau === 1 ? 2 : progression.niveau === 2 ? 3 : 4
  pieces.value = melanger(taille.value * taille.value)
  choix.value = null
  coups.value = 0
  message.value = ''
  etoiles.value = 0
  points.value = 0
  etape.value = 'jeu'
}

function stylePiece(pieceIndex) {
  const n = taille.value
  const rangee = Math.floor(pieceIndex / n)
  const colonne = pieceIndex % n
  return {
    backgroundImage: `url("${IMAGE_URI}")`,
    backgroundSize: `${n * 100}% ${n * 100}%`,
    backgroundPosition: `${(colonne * 100) / (n - 1)}% ${(rangee * 100) / (n - 1)}%`,
  }
}

const styleImageComplete = {
  backgroundImage: `url("${IMAGE_URI}")`,
  backgroundSize: 'cover',
}

function choisirPiece(index) {
  if (choix.value === null) {
    choix.value = index
    message.value = ''
    return
  }
  if (choix.value === index) {
    choix.value = null
    return
  }
  ;[pieces.value[choix.value], pieces.value[index]] = [pieces.value[index], pieces.value[choix.value]]
  coups.value += 1
  choix.value = null
  message.value = ''
  if (pieces.value.every((piece, position) => piece === position)) terminer()
}

function terminer() {
  const nbCases = taille.value * taille.value
  points.value = Math.max(30, nbCases * 40 - coups.value * 10)
  etoiles.value = coups.value <= nbCases ? 3 : coups.value <= nbCases * 2 ? 2 : 1
  noterScore('puzzle', progression.niveau, points.value, etoiles.value)
  API.envoyerScore({
    pseudo: progression.pseudo,
    jeu: 'puzzle',
    niveau: progression.niveau,
    points: points.value,
    etoiles: etoiles.value,
  })
  etape.value = 'fin'
}

watch(() => progression.niveau, () => {
  if (etape.value !== 'fin') etape.value = 'accueil'
})
</script>

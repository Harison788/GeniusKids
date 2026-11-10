<template>
  <section class="jeu">
    <h1 class="titre-jeu">Relie les points</h1>

    <p v-if="erreur" class="message-erreur">
      {{ erreur }}<br />
      <button class="btn-gros" @click="demarrer">Réessayer</button>
    </p>

    <template v-if="etape === 'accueil'">
      <p class="rappel-niveau">Touche les numéros dans l'ordre, de 1 jusqu'à la fin, pour découvrir le dessin secret.</p>
      <button class="btn-gros" @click="demarrer">C'est parti !</button>
    </template>

    <template v-else-if="etape === 'jeu' && forme">
      <p class="compteur">Point suivant : n° {{ prochain + 1 }} sur {{ forme.points.length }} • Erreurs : {{ erreurs }}</p>
      <p class="message-feedback" v-if="message">{{ message }}</p>

      <svg viewBox="0 0 100 100" class="svg-points" role="img" :aria-label="forme.nom">
        <polyline class="trait-points" :points="cheminTrace" />
        <polygon
          v-if="termine"
          class="forme-remplie"
          :points="cheminTrace"
        />
        <g v-for="(point, i) in forme.points" :key="i">
          <circle
            class="point-cercle"
            :cx="point[0]"
            :cy="point[1]"
            r="3.2"
            :class="{ 'est-select': i === prochain, 'est-fait': i < prochain }"
          />
          <circle
            class="cible-point"
            :cx="point[0]"
            :cy="point[1]"
            r="7"
            @click="choisirPoint(i)"
          />
          <text :x="point[0]" :y="point[1] - 4.6">{{ i + 1 }}</text>
        </g>
      </svg>
    </template>

    <template v-else-if="etape === 'fin' && forme">
      <div class="carte-gagnant">
        <p class="etoiles-grandes">{{ '★'.repeat(etoiles) + '☆'.repeat(3 - etoiles) }}</p>
        <p class="score-final">Score : {{ points }} points</p>
        <p class="dessin-revele">{{ forme.emoji }}<br /><strong>{{ forme.nom }}</strong></p>
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

const FORMES = [
  { nom: 'La maison', emoji: '🏠', niveau: 1, points: [[50, 6], [12, 40], [22, 92], [78, 92], [88, 40]] },
  { nom: 'Le bateau', emoji: '⛵', niveau: 1, points: [[50, 8], [18, 64], [82, 64], [92, 76], [8, 76]] },
  { nom: 'Le poisson', emoji: '🐟', niveau: 2, points: [[8, 50], [40, 25], [70, 30], [92, 25], [80, 50], [92, 75], [70, 70], [40, 75]] },
  {
    nom: 'L\'étoile', emoji: '⭐', niveau: 2,
    points: [[50, 5], [61.8, 33.8], [92.8, 36.1], [69, 56.2], [76.5, 86.4], [50, 70], [23.5, 86.4], [31, 56.2], [7.2, 36.1], [38.2, 33.8]],
  },
  { nom: 'Le sapin', emoji: '🎄', niveau: 3, points: [[50, 8], [35, 30], [42, 30], [25, 55], [35, 55], [15, 80], [85, 80], [65, 55], [75, 55], [58, 30], [65, 30]] },
  {
    nom: 'Le soleil', emoji: '☀️', niveau: 3,
    points: [[50, 4], [56.9, 33.4], [82.5, 17.5], [66.6, 43.1], [96, 50], [66.6, 56.9], [82.5, 82.5], [56.9, 66.6], [50, 96], [43.1, 66.6], [17.5, 82.5], [33.4, 56.9], [4, 50], [33.4, 43.1], [17.5, 17.5], [43.1, 33.4]],
  },
]

const etape = ref('accueil')
const erreur = ref('')
const forme = ref(null)
const prochain = ref(0)
const erreurs = ref(0)
const message = ref('')
const etoiles = ref(0)
const points = ref(0)

const termine = computed(() => forme.value && prochain.value >= forme.value.points.length)
const cheminTrace = computed(() => {
  if (!forme.value) return ''
  const passe = forme.value.points.slice(0, Math.min(prochain.value + 1, forme.value.points.length))
  return passe.map((point) => point.join(',')).join(' ')
})

function choisirForme() {
  const possibles = FORMES.filter((f) => f.niveau === progression.niveau)
  const liste = possibles.length ? possibles : FORMES
  return liste[Math.floor(Math.random() * liste.length)]
}

async function demarrer() {
  // API appelée pour rester cohérent avec les autres jeux (et vérifier le serveur)
  erreur.value = ''
  message.value = ''
  etoiles.value = 0
  etape.value = 'chargement'
  try {
    await API.charger('quiz', progression.niveau) // ping simple du serveur
    forme.value = choisirForme()
    prochain.value = 0
    erreurs.value = 0
    etape.value = 'jeu'
  } catch {
    erreur.value = 'Oups, impossible de lancer le jeu. Le serveur tourne-t-il ?'
    etape.value = 'accueil'
  }
}

function choisirPoint(index) {
  if (termine.value) return
  if (index < prochain.value) return
  if (index === prochain.value) {
    prochain.value += 1
    message.value = ''
    if (termine.value) terminer()
  } else {
    erreurs.value += 1
    message.value = `Ce n'est pas le numéro ${index + 1}, cherche le n° ${prochain.value + 1} !`
  }
}

function terminer() {
  const total = forme.value.points.length
  points.value = Math.max(10, total * 10 - erreurs.value * 5)
  etoiles.value = erreurs.value === 0 ? 3 : erreurs.value <= 3 ? 2 : 1
  noterScore('points', progression.niveau, points.value, etoiles.value)
  API.envoyerScore({
    pseudo: progression.pseudo,
    jeu: 'points',
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

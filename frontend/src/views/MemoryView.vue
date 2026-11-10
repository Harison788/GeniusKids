<template>
  <section class="jeu">
    <h1 class="titre-jeu">🃏 Memory</h1>

    <p v-if="erreur" class="message-erreur">
      {{ erreur }}<br />
      <button class="btn-gros" @click="demarrer">Réessayer</button>
    </p>

    <template v-if="etape === 'accueil'">
      <button class="btn-gros" @click="demarrer">C'est parti !</button>
      <p class="rappel-niveau">Retourne 2 cartes et trouve les paires !</p>
    </template>
    <template v-else-if="etape === 'jeu'">
      <p class="compteur">Paires trouvées : {{ trouvees.length }} / {{ nbPaires }} • Essais : {{ essais }}</p>
      <div class="plateau-memory">
        <button
          v-for="(carte, index) in cartes"
          :key="index"
          class="carte-memory"
          :class="{ 'est-visible': carte.retournee || carte.trouvee, 'est-trouvee': carte.trouvee }"
          @click="retourner(index)"
        >
          <span v-if="carte.retournee || carte.trouvee" class="face-carte">{{ carte.texte }}</span>
          <span v-else class="dos-carte">❓</span>
        </button>
      </div>
    </template>

    <template v-else-if="etape === 'fin'">
      <div class="carte-gagnant">
        <p class="etoiles-grandes">{{ '⭐'.repeat(etoiles) + '☆'.repeat(3 - etoiles) }}</p>
        <p class="score-final">Score : {{ points }} points</p>
        <p class="bravo">Toutes les paires trouvées en {{ essais }} essais ! 🎉</p>
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

const etape = ref('accueil')
const erreur = ref('')
const cartes = ref([])
const retournees = ref([])
const trouvees = ref([])
const bloque = ref(false)
const essais = ref(0)
const etoiles = ref(0)
const points = ref(0)

const nbPaires = ref(0)

async function demarrer() {
  erreur.value = ''
  etape.value = 'chargement'
  try {
    const donnees = await API.charger('memory', progression.niveau)
    nbPaires.value = donnees.paires.length
    const deck = donnees.paires.flatMap((paire) => [
      { paireId: paire.id, texte: paire.gauche, retournee: false, trouvee: false },
      { paireId: paire.id, texte: paire.droite, retournee: false, trouvee: false },
    ])
    // Mélange de Fisher-Yates
    for (let i = deck.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[deck[i], deck[j]] = [deck[j], deck[i]]
    }
    cartes.value = deck
    retournees.value = []
    trouvees.value = []
    essais.value = 0
    points.value = 0
    bloque.value = false
    etape.value = 'jeu'
  } catch {
    erreur.value = 'Oups, impossible de lancer le jeu. Le serveur tourne-t-il ?'
    etape.value = 'accueil'
  }
}

function retourner(index) {
  if (bloque.value || etape.value !== 'jeu') return
  const carte = cartes.value[index]
  if (!carte || carte.trouvee || carte.retournee) return

  carte.retournee = true
  retournees.value.push(index)
  if (retournees.value.length < 2) return

  essais.value += 1
  const [premiere, deuxieme] = retournees.value.map((i) => cartes.value[i])
  if (premiere.paireId === deuxieme.paireId) {
    premiere.trouvee = true
    deuxieme.trouvee = true
    trouvees.value.push(premiere.paireId)
    retournees.value = []
    if (trouvees.value.length === nbPaires.value) terminer()
  } else {
    bloque.value = true
    setTimeout(() => {
      premiere.retournee = false
      deuxieme.retournee = false
      retournees.value = []
      bloque.value = false
    }, 800)
  }
}

function terminer() {
  points.value = Math.max(10, nbPaires.value * 20 - essais.value * 2)
  etoiles.value =
    essais.value <= nbPaires.value + 1 ? 3 : essais.value <= nbPaires.value * 2 ? 2 : 1
  noterScore('memory', progression.niveau, points.value, etoiles.value)
  API.envoyerScore({
    pseudo: progression.pseudo,
    jeu: 'memory',
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

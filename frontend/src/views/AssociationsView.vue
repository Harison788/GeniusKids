<template>
  <section class="jeu">
    <h1 class="titre-jeu">🔗 Associations</h1>

    <p v-if="erreur" class="message-erreur">
      {{ erreur }}<br />
      <button class="btn-gros" @click="demarrer">Réessayer</button>
    </p>

    <template v-if="etape === 'accueil'">
      <button class="btn-gros" @click="demarrer">C'est parti !</button>
      <p class="rappel-niveau">Touche une carte à gauche, puis celle qui va avec à droite !</p>
    </template>

    <template v-else-if="etape === 'jeu'">
      <p class="theme-titre">{{ theme }}</p>
      <p class="compteur">Trouvées : {{ nbTrouvees }} / {{ total }} • Essais : {{ essais }}</p>

      <div class="plateau-associations">
        <div class="colonne-association">
          <button
            v-for="item in colonneGauche"
            :key="'g' + item.id"
            class="carte-association"
            :class="{ 'est-choisie': selection === item.id, 'est-appariee': item.apparie }"
            :disabled="item.apparie"
            @click="choisirGauche(item)"
          >
            {{ item.texte }}
          </button>
        </div>
        <div class="colonne-association">
          <button
            v-for="item in colonneDroite"
            :key="'d' + item.id"
            class="carte-association"
            :class="{ 'est-appariee': item.apparie }"
            :disabled="item.apparie"
            @click="choisirDroite(item)"
          >
            {{ item.texte }}
          </button>
        </div>
      </div>

      <p class="message-feedback" v-if="message">{{ message }}</p>
    </template>

    <template v-else-if="etape === 'fin'">
      <div class="carte-gagnant">
        <p class="etoiles-grandes">{{ '⭐'.repeat(etoiles) + '☆'.repeat(3 - etoiles) }}</p>
        <p class="score-final">Score : {{ points }} points</p>
        <p class="bravo">Tout est relié, bravo ! 🎉</p>
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

const etape = ref('accueil')
const erreur = ref('')
const theme = ref('')
const colonneGauche = ref([])
const colonneDroite = ref([])
const selection = ref(null)
const essais = ref(0)
const message = ref('')
const etoiles = ref(0)
const points = ref(0)

const nbTrouvees = computed(() => colonneDroite.value.filter((i) => i.apparie).length)
const total = computed(() => colonneDroite.value.length)

function melanger(liste) {
  const copie = [...liste]
  for (let i = copie.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[copie[i], copie[j]] = [copie[j], copie[i]]
  }
  return copie
}

async function demarrer() {
  erreur.value = ''
  message.value = ''
  selection.value = null
  essais.value = 0
  etape.value = 'chargement'
  try {
    const donnees = await API.charger('associations', progression.niveau)
    theme.value = donnees.theme
    colonneGauche.value = melanger(
      donnees.paires.map((p) => ({ id: p.id, texte: p.gauche, apparie: false }))
    )
    colonneDroite.value = melanger(
      donnees.paires.map((p) => ({ id: p.id, texte: p.droite, apparie: false }))
    )
    etape.value = 'jeu'
  } catch {
    erreur.value = 'Oups, impossible de lancer le jeu. Le serveur tourne-t-il ?'
    etape.value = 'accueil'
  }
}

function choisirGauche(item) {
  if (item.apparie) return
  selection.value = item.id
  message.value = ''
}

function choisirDroite(item) {
  if (item.apparie || selection.value === null) return
  essais.value += 1
  if (selection.value === item.id) {
    item.apparie = true
    const gaucheAppariee = colonneGauche.value.find((g) => g.id === item.id)
    if (gaucheAppariee) gaucheAppariee.apparie = true
    selection.value = null
    message.value = 'Super !'    if (nbTrouvees.value === total.value) terminer()
  } else {
    selection.value = null
    message.value = '🤔 Essaie encore !'
  }
}

function terminer() {
  const nbPaires = total.value
  points.value = Math.max(10, nbPaires * 20 - essais.value * 2)
  etoiles.value =
    essais.value <= nbPaires + 1 ? 3 : essais.value <= nbPaires * 2 ? 2 : 1
  noterScore('associations', progression.niveau, points.value, etoiles.value)
  API.envoyerScore({
    pseudo: progression.pseudo,
    jeu: 'associations',
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

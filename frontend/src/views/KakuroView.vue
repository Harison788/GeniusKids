<template>
  <section class="jeu">
    <h1 class="titre-jeu">Kakuro</h1>

    <p v-if="erreur" class="message-erreur">
      {{ erreur }}<br />
      <button class="btn-gros" @click="demarrer">Réessayer</button>
    </p>

    <template v-if="etape === 'accueil'">
      <p class="rappel-niveau">Remplis les cases pour que chaque ligne et chaque colonne fasse la bonne somme.</p>
      <button class="btn-gros" @click="demarrer">C'est parti !</button>
    </template>

    <template v-else-if="etape === 'jeu' && donnees">
      <div class="grille-kakuro" :style="{ '--colonnes-kakuro': donnees.taille + 1 }">
        <div class="cellule-kakuro entete-kakuro"></div>
        <div
          v-for="(cible, col) in donnees.cibleColonnes"
          :key="'tete-col-' + col"
          class="cellule-kakuro entete-kakuro"
          :class="{ 'est-validee': colonnesOk[col] }"
        >
          <span class="fleche">↓</span> {{ cible }}
        </div>

        <template v-for="(cible, ligne) in donnees.cibleLignes" :key="'ligne-' + ligne">
          <div class="cellule-kakuro entete-kakuro" :class="{ 'est-validee': lignesOk[ligne] }">
            <span class="fleche">→</span> {{ cible }}
          </div>
          <div
            v-for="col in donnees.taille"
            :key="'case-' + ligne + '-' + col"
            class="cellule-kakuro case-kakuro"
            :class="{ 'est-choisie': caseChoisie(ligne, col - 1) }"
            @click="choisirCase(ligne, col - 1)"
          >
            {{ valeurs[ligne]?.[col - 1] ?? '' }}
          </div>
        </template>
      </div>

      <div class="pave-chiffres">
        <button
          v-for="n in 9"
          :key="n"
          class="btn-chiffre"
          :disabled="!selection"
          @click="poserChiffre(n)"
        >
          {{ n }}
        </button>
        <button class="btn-chiffre btn-effacer" :disabled="!selection" @click="effacerCase">Effacer</button>
        <button class="btn-chiffre btn-indice" @click="donnerIndice">Indice</button>
      </div>

      <p class="compteur">
        Lignes validées : {{ nbLignesOk }} / {{ donnees.taille }}
        • Colonnes validées : {{ nbColonnesOk }} / {{ donnees.taille }} • Indices : {{ indices }}
      </p>
    </template>

    <template v-else-if="etape === 'fin'">
      <div class="carte-gagnant">
        <p class="etoiles-grandes">{{ '★'.repeat(etoiles) + '☆'.repeat(3 - etoiles) }}</p>
        <p class="score-final">Score : {{ points }} points</p>
        <p class="bravo">Le Kakuro est terminé, bravo !</p>
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
const donnees = ref(null)
const valeurs = ref([])
const selection = ref(null)
const lignesOk = ref([])
const colonnesOk = ref([])
const indices = ref(0)
const etoiles = ref(0)
const points = ref(0)

const nbLignesOk = computed(() => lignesOk.value.filter(Boolean).length)
const nbColonnesOk = computed(() => colonnesOk.value.filter(Boolean).length)

async function demarrer() {
  erreur.value = ''
  etape.value = 'chargement'
  try {
    const reponse = await API.charger('kakuro', progression.niveau)
    donnees.value = reponse
    valeurs.value = Array.from({ length: reponse.taille }, () =>
      Array(reponse.taille).fill(null)
    )
    lignesOk.value = Array(reponse.taille).fill(false)
    colonnesOk.value = Array(reponse.taille).fill(false)
    selection.value = null
    indices.value = 0
    etoiles.value = 0
    points.value = 0
    etape.value = 'jeu'
  } catch {
    erreur.value = 'Oups, impossible de lancer le jeu. Le serveur tourne-t-il ?'
    etape.value = 'accueil'
  }
}

function caseChoisie(ligne, colonne) {
  const sel = selection.value
  return !!sel && sel.ligne === ligne && sel.colonne === colonne
}

function choisirCase(ligne, colonne) {
  selection.value = { ligne, colonne }
}

function poserChiffre(n) {
  const sel = selection.value
  if (!sel) return
  valeurs.value[sel.ligne][sel.colonne] = n
  verifier()
}

function effacerCase() {
  const sel = selection.value
  if (!sel) return
  valeurs.value[sel.ligne][sel.colonne] = null
  verifier()
}

function verifier() {
  const taille = donnees.value.taille
  lignesOk.value = donnees.value.cibleLignes.map((cible, ligne) => {
    const rangee = valeurs.value[ligne]
    return rangee.every((v) => v !== null) && rangee.reduce((a, b) => a + b, 0) === cible
  })
  colonnesOk.value = donnees.value.cibleColonnes.map((cible, colonne) => {
    const colonneValeurs = valeurs.value.map((rangee) => rangee[colonne])
    return colonneValeurs.every((v) => v !== null) && colonneValeurs.reduce((a, b) => a + b, 0) === cible
  })
  const toutValide = lignesOk.value.every(Boolean) && colonnesOk.value.every(Boolean)
  if (toutValide && taille > 0) terminer()
}

function donnerIndice() {
  const taille = donnees.value.taille
  const candidats = []
  for (let ligne = 0; ligne < taille; ligne += 1) {
    for (let colonne = 0; colonne < taille; colonne += 1) {
      if (valeurs.value[ligne][colonne] !== donnees.value.solution[ligne][colonne]) {
        candidats.push({ ligne, colonne })
      }
    }
  }
  if (!candidats.length) return
  const choix = candidats[Math.floor(Math.random() * candidats.length)]
  valeurs.value[choix.ligne][choix.colonne] = donnees.value.solution[choix.ligne][choix.colonne]
  indices.value += 1
  selection.value = choix
  verifier()
}

function terminer() {
  const nbCases = donnees.value.taille ** 2
  points.value = Math.max(20, nbCases * 30 - indices.value * 20)
  etoiles.value = indices.value === 0 ? 3 : indices.value <= 2 ? 2 : 1
  noterScore('kakuro', progression.niveau, points.value, etoiles.value)
  API.envoyerScore({
    pseudo: progression.pseudo,
    jeu: 'kakuro',
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

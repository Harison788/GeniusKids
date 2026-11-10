<template>
  <section class="recompenses">
    <h1 class="titre-page">Mes récompenses</h1>

    <div class="carte-total">
      <span class="emoji-total">🏆</span>
      <div class="texte-total">
        <p class="nombre-total">{{ progression.etoiles }} étoiles</p>
        <p class="sous-total">Gagnées en jouant, à ton rythme !</p>
      </div>
    </div>

    <template v-if="liste.length > 0">
      <div class="liste-records">
        <div v-for="entree in liste" :key="entree.cle" class="rangee-record">
          <span class="emoji-record">{{ entree.emoji }}</span>
          <span class="titre-record">{{ entree.titre }}</span>
          <span class="niveau-record">{{ entree.nomNiveau }}</span>
          <span class="points-record">{{ entree.points }} pts</span>
          <span class="etoiles-record">{{ '⭐'.repeat(entree.etoiles) }}</span>
        </div>
      </div>
    </template>

    <template v-else>
      <div class="carte-vide">
        <p class="emoji-vide">🌱</p>
        <p>Pas encore de record. Lance un jeu et reviens brandir ton trophée !</p>
        <RouterLink to="/" class="btn-gros">Choisir un jeu</RouterLink>
      </div>
    </template>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'
import { progression } from '../stores/progression'

const TITRES = {
  quiz: { titre: 'Quiz de Maths', emoji: '🧮' },
  comptage: { titre: 'Comptage', emoji: '🔢' },
  memory: { titre: 'Memory', emoji: '🃏' },
  associations: { titre: 'Associations', emoji: '🔗' },
  kakuro: { titre: 'Kakuro', emoji: '🧩' },
  points: { titre: 'Relie les Points', emoji: '✏️' },
  fruits: { titre: 'Fusion des Fruits', emoji: '🍓' },
  puzzle: { titre: 'Puzzle', emoji: '🖼️' },
}

const NOMS_NIVEAUX = { 1: 'Écureuil', 2: 'Renard', 3: 'Hibou' }

const liste = computed(() =>
  Object.entries(progression.meilleures)
    .map(([cle, valeur]) => {
      const [jeu, niveau] = cle.split('-')
      const info = TITRES[jeu] ?? { titre: jeu, emoji: '🎯' }
      return {
        cle,
        titre: info.titre,
        emoji: info.emoji,
        nomNiveau: NOMS_NIVEAUX[Number(niveau)] ?? `Niveau ${niveau}`,
        points: valeur.points,
        etoiles: valeur.etoiles,
      }
    })
    .sort((a, b) => a.titre.localeCompare(b.titre) || a.nomNiveau.localeCompare(b.nomNiveau)),
)
</script>

<template>
  <section class="mx-auto max-w-3xl">
    <h1 class="text-2xl font-extrabold text-purple-900">Mes récompenses</h1>

    <!-- Trophée total -->
    <div class="mt-4 flex items-center gap-4 rounded-3xl bg-gradient-to-r from-amber-300 to-amber-400 p-5 text-amber-900 shadow-sm">
      <span class="text-5xl leading-none">🏆</span>
      <div>
        <p class="text-xl font-extrabold">{{ progression.etoiles }} étoiles</p>
        <p class="text-sm font-bold text-amber-800/80">Gagnées en jouant, à ton rythme !</p>
      </div>
    </div>

    <!-- Liste des records -->
    <div
      v-if="liste.length > 0"
      class="mt-4 divide-y divide-purple-50 rounded-3xl border border-purple-100 bg-white shadow-sm"
    >
      <div
        v-for="entree in liste"
        :key="entree.cle"
        class="flex items-center gap-3 px-5 py-3"
      >
        <span class="text-2xl leading-none">{{ entree.emoji }}</span>
        <span class="flex-1 font-extrabold text-slate-800">{{ entree.titre }}</span>
        <span class="text-xs font-bold text-slate-400">{{ entree.nomNiveau }}</span>
        <span class="font-extrabold text-purple-600">{{ entree.points }} pts</span>
        <span class="w-20 text-right tracking-wide">{{ '⭐'.repeat(entree.etoiles) }}</span>
      </div>
    </div>

    <!-- Vide -->
    <div v-else class="mt-4 flex flex-col items-center gap-3 rounded-3xl border border-purple-100 bg-white p-8 text-center shadow-sm">
      <span class="text-5xl">🌱</span>
      <p class="font-bold text-slate-600">Pas encore de record. Lance un jeu et reviens brandir ton trophée !</p>
      <RouterLink
        to="/"
        class="rounded-full bg-purple-700 px-8 py-3 font-extrabold text-white transition-colors hover:bg-purple-800"
      >
        Choisir un jeu
      </RouterLink>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'
import { progression } from '../stores/progression'

const TITRES = {
  quiz: { titre: 'Quiz Maths', emoji: '➕' },
  comptage: { titre: 'Comptage', emoji: '🧮' },
  memory: { titre: 'Memory', emoji: '⭐' },
  associations: { titre: 'Associations', emoji: '🔗' },
  kakuro: { titre: 'Kakuro', emoji: '🔢' },
  points: { titre: 'Relie les Points', emoji: '✏️' },
  fruits: { titre: 'Fusion des fruits', emoji: '🍑' },
  puzzle: { titre: 'Puzzles', emoji: '🧩' },
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

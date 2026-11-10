<template>
  <div>
    <!-- Titre de section -->
    <div class="mb-4">
      <h2 class="text-2xl font-extrabold text-purple-900">À toi de jouer !</h2>
      <p class="text-sm font-semibold text-slate-500">Un petit jeu, de grandes découvertes.</p>
    </div>

    <!-- Filtres par catégorie -->
    <div class="mb-5 flex flex-wrap gap-2">
      <button
        v-for="f in filtres"
        :key="f.cle"
        class="rounded-full px-4 py-2 text-sm font-bold transition-colors"
        :class="filtreActif === f.cle
          ? 'bg-purple-700 text-white'
          : 'bg-slate-100 text-slate-600 hover:bg-slate-200'"
        @click="filtreActif = f.cle"
      >
        {{ f.label }}
      </button>
    </div>

    <!-- Grille des mini-jeux -->
    <div id="jeux" class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      <article
        v-for="jeu in jeuxAffiches"
        :key="jeu.slug"
        class="flex flex-col items-center rounded-3xl p-5 text-center transition-transform hover:-translate-y-1"
        :style="{ backgroundColor: jeu.couleur_carte || '#f3f0ff' }"
      >
        <!-- Illustration -->
        <img
          v-if="jeu.image_url"
          :src="jeu.image_url"
          :alt="jeu.title"
          class="h-20 w-20 rounded-2xl object-cover"
        />
        <GameIllustration v-else :slug="jeu.slug" :taille="88" />

        <h3 class="mt-4 text-lg font-extrabold text-slate-800">{{ jeu.title }}</h3>
        <p class="mt-0.5 text-sm font-semibold text-slate-500">{{ jeu.description }}</p>

        <RouterLink
          :to="`/${jeu.slug}`"
          class="mt-4 w-full rounded-full border border-purple-100 bg-white py-2.5 text-sm font-extrabold text-purple-700 shadow-sm transition-transform hover:scale-[1.02]"
        >
          Jouer
        </RouterLink>
      </article>
    </div>

    <p v-if="jeuxAffiches.length === 0" class="py-8 text-center font-semibold text-slate-400">
      Aucun jeu dans cette catégorie pour l'instant.
    </p>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import API from '../api'
import GameIllustration from './GameIllustration.vue'

const filtres = [
  { cle: 'tous', label: 'Tous les jeux' },
  { cle: 'nombres', label: 'Nombres' },
  { cle: 'memoire', label: 'Mémoire' },
  { cle: 'creativite', label: 'Créativité' },
]

const filtreActif = ref('tous')
const jeux = ref([])
const chargement = ref(true)

onMounted(async () => {
  try {
    jeux.value = await API.chargerJeux()
  } catch {
    // Backend éteint : liste de secours pour que l'enfant puisse jouer quand même.
    jeux.value = [
      { slug: 'quiz', title: 'Quiz Maths', description: 'Joue avec les nombres', category: 'nombres', emoji: '➕', couleur_carte: '#f3f0ff' },
      { slug: 'memory', title: 'Memory', description: 'Trouve les paires', category: 'memoire', emoji: '⭐', couleur_carte: '#e9e4fb' },
      { slug: 'fruits', title: 'Fusion des fruits', description: 'Fais le plein de fruits !', category: 'creativite', emoji: '🍑', couleur_carte: '#fdeedd' },
      { slug: 'puzzle', title: 'Puzzles', description: 'Assemble et découvre', category: 'creativite', emoji: '🧩', couleur_carte: '#ddf2e9' },
      { slug: 'kakuro', title: 'Kakuro', description: 'À toi de calculer !', category: 'nombres', emoji: '🔢', couleur_carte: '#e9e4fb' },
      { slug: 'comptage', title: 'Comptage', description: 'Compte avec nous', category: 'nombres', emoji: '🧮', couleur_carte: '#fef3c7' },
    ]
  } finally {
    chargement.value = false
  }
})

const jeuxAffiches = computed(() => {
  if (filtreActif.value === 'tous') return jeux.value
  return jeux.value.filter((jeu) => jeu.category === filtreActif.value)
})
</script>

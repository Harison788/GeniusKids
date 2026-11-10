<template>
  <div>
    <!-- Titre de section (sous-titre sur la même ligne, comme la maquette) -->
    <div class="mb-4 flex flex-wrap items-baseline gap-x-10 gap-y-1">
      <h2 class="text-[1.4rem] font-extrabold text-[#6d28d9]">À toi de jouer !</h2>
      <p class="text-[0.85rem] font-medium text-slate-400">Un petit jeu, de grandes découvertes.</p>
    </div>

    <!-- Filtres par catégorie -->
    <div class="mb-5 flex flex-wrap gap-2.5">
      <button
        v-for="f in filtres"
        :key="f.cle"
        class="rounded-full px-4 py-1.5 text-[0.82rem] font-bold transition-colors"
        :class="filtreActif === f.cle
          ? 'bg-[#6d28d9] text-white'
          : 'bg-[#ececf3] text-slate-600 hover:bg-[#e2e2ec]'"
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
        class="flex flex-col rounded-[20px] p-4 pb-5 transition-transform hover:-translate-y-0.5"
        :style="{ backgroundColor: jeu.couleur_carte || '#e9e4fb' }"
      >
        <!-- Illustration centrée, textes alignés à gauche comme la maquette -->
        <img
          v-if="jeu.image_url"
          :src="jeu.image_url"
          :alt="jeu.title"
          class="mx-auto my-2 h-20 w-20 object-cover"
        />
        <GameIllustration v-else :slug="jeu.slug" :taille="84" class="my-3" />

        <h3 class="mt-2 text-[1.05rem] font-extrabold text-[#2d2a45]">{{ jeu.title }}</h3>
        <p class="mt-0.5 text-[0.85rem] font-medium text-slate-600">{{ jeu.description }}</p>

        <RouterLink
          :to="`/${jeu.slug}`"
          class="mt-4 w-full rounded-full bg-white py-2.5 text-center text-[0.9rem] font-extrabold text-[#6d28d9] shadow-[0_3px_10px_rgba(90,60,160,0.14)] transition-shadow hover:shadow-[0_5px_16px_rgba(90,60,160,0.2)]"
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
    // Backend éteint : liste de secours avec les couleurs de la maquette.
    jeux.value = [
      { slug: 'quiz', title: 'Quiz Maths', description: 'Joue avec les nombres', category: 'nombres', emoji: '➕', couleur_carte: '#e3d7fa' },
      { slug: 'memory', title: 'Memory', description: 'Trouve les paires', category: 'memoire', emoji: '⭐', couleur_carte: '#ded9fb' },
      { slug: 'fruits', title: 'Fusion des fruits', description: 'Fais le plein de fruits !', category: 'creativite', emoji: '🍑', couleur_carte: '#fbe3d3' },
      { slug: 'puzzle', title: 'Puzzles', description: 'Assemble et découvre', category: 'creativite', emoji: '🧩', couleur_carte: '#d9f0e6' },
      { slug: 'kakuro', title: 'Kakuro', description: 'À toi de calculer !', category: 'nombres', emoji: '🔢', couleur_carte: '#ddd5fa' },
      { slug: 'comptage', title: 'Comptage', description: 'Compte avec nous', category: 'nombres', emoji: '🧮', couleur_carte: '#fdf2cc' },
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

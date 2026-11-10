<template>
  <div class="appli">
    <header class="entete">
      <RouterLink to="/" class="logo">
        <span class="logo-emoji">🧮</span>
        <span class="logo-texte">Les Petits Génies</span>
      </RouterLink>
      <nav class="menu">
        <RouterLink to="/quiz" class="lien-menu">Quiz</RouterLink>
        <RouterLink to="/comptage" class="lien-menu">Comptage</RouterLink>
        <RouterLink to="/memory" class="lien-menu">Memory</RouterLink>
        <RouterLink to="/associations" class="lien-menu">Associations</RouterLink>
        <RouterLink to="/kakuro" class="lien-menu">Kakuro</RouterLink>
        <RouterLink to="/points" class="lien-menu">Relie les points</RouterLink>
        <RouterLink to="/fruits" class="lien-menu">Fruits</RouterLink>
        <RouterLink to="/puzzle" class="lien-menu">Puzzle</RouterLink>
      </nav>
      <div class="badge-etoiles" title="Tes étoiles">⭐ {{ progression.etoiles }}</div>
    </header>

    <main class="contenu">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { progression } from './stores/progression'
</script>

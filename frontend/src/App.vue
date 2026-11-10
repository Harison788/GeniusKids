<template>
  <div class="appli-fond flex min-h-screen flex-col font-sans text-slate-800">
    <Navbar />

    <!-- Décor du thème choisi (fleurs, voitures...) en fond de page -->
    <span class="deco-theme gauche" aria-hidden="true"></span>
    <span class="deco-theme droite" aria-hidden="true"></span>

    <main class="relative z-[1] mx-auto w-full max-w-7xl flex-1 px-4 py-6 sm:px-6">
      <RouterView />
    </main>

    <Footer />
  </div>
</template>

<script setup>
import { watch, onMounted } from 'vue'
import { RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import { apparence, chargerApparenceDistante } from './stores/apparence'
import { chargerProgressionDistante } from './stores/progression'

/* Le thème choisi colore le fond de la page entière. */
function appliquerTheme() {
  document.body.dataset.theme = apparence.theme
}

watch(() => apparence.theme, appliquerTheme)

onMounted(async () => {
  appliquerTheme()
  await chargerApparenceDistante()
  await chargerProgressionDistante()
  appliquerTheme()
})
</script>

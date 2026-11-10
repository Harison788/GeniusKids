<template>
  <div class="flex flex-wrap items-center gap-5 rounded-3xl bg-[#f3f0ff] p-6 sm:p-7">
    <!-- Avatar + textes -->
    <span
      class="grid h-16 w-16 shrink-0 place-items-center rounded-full bg-white text-4xl shadow-sm"
      aria-hidden="true"
    >
      {{ apparence.avatar }}
    </span>

    <div class="min-w-0 flex-1">
      <h1 class="text-2xl font-extrabold text-slate-800 sm:text-[1.7rem]">
        Bonjour {{ progression.pseudo }} !
      </h1>
      <p class="mt-0.5 font-bold text-slate-700">Prêt à t'amuser ?</p>
      <p class="mt-0.5 text-sm font-semibold text-slate-500">
        Apprendre en s'amusant, à ton rythme.
      </p>
    </div>

    <!-- Carte étoiles -->
    <div class="ml-auto rounded-2xl border border-purple-100 bg-white px-6 py-4 text-center shadow-sm">
      <p class="flex items-center justify-center gap-2 text-lg font-extrabold text-purple-700">
        <EtoileSvg :taille="20" /> {{ progression.etoiles }} étoiles
      </p>
      <p class="mt-1 text-sm font-semibold text-slate-500">
        Bravo, {{ progression.pseudo === 'Petit curieux' ? 'petit curieux' : progression.pseudo }} !
      </p>
    </div>
  </div>
</template>

<script setup>
import { progression } from '../stores/progression'
import { apparence } from '../stores/apparence'
import EtoileSvg from './EtoileSvg.vue'
</script>

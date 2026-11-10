<template>
  <aside class="flex flex-col gap-5">
    <!-- Mon coin à moi -->
    <div>
      <h2 class="mb-3 text-lg font-extrabold text-slate-800">Mon coin à moi</h2>

      <div class="rounded-3xl border border-purple-100 bg-white p-4 shadow-sm">
        <div class="flex items-center gap-3">
          <span class="grid h-14 w-14 shrink-0 place-items-center rounded-full bg-purple-50 text-3xl leading-none">
            {{ apparence.avatar }}
          </span>
          <div class="min-w-0">
            <p class="truncate font-extrabold text-slate-800">{{ apparence.avatarNom }}</p>
            <p class="text-sm font-semibold text-slate-400">C'est toi !</p>
          </div>
        </div>

        <button
          class="mt-4 w-full rounded-full border border-purple-200 py-2.5 text-sm font-extrabold text-purple-700 transition-colors hover:bg-purple-50"
          @click="$emit('personnaliser', 'profil')"
        >
          Personnaliser mon animal
        </button>

        <button
          class="mt-2 w-full rounded-full py-1.5 text-xs font-bold text-slate-400 transition-colors hover:bg-slate-50 hover:text-purple-600"
          @click="$emit('personnaliser', 'themes')"
        >
          {{ themeActuel().emoji }} Changer le thème du jeu
        </button>
      </div>
    </div>

    <!-- Milo la mascotte -->
    <div class="rounded-3xl bg-[#f3f0ff] p-4">
      <div class="rounded-2xl bg-purple-600 p-4 text-white shadow-sm">
        <p class="font-extrabold">Coucou, moi c'est Milo !</p>
        <p class="mt-0.5 text-sm font-semibold text-purple-100">
          Choisis un jeu et amuse-toi !
        </p>
      </div>

      <div class="my-2 flex justify-center">
        <MascotMilo :taille="110" class="-rotate-3" />
      </div>

      <p class="text-center text-sm font-extrabold text-purple-700">
        À chaque jeu,<br />une découverte !
      </p>
    </div>
  </aside>
</template>

<script setup>
import MascotMilo from './MascotMilo.vue'
import { apparence, themeActuel } from '../stores/apparence'

defineEmits(['personnaliser'])
</script>

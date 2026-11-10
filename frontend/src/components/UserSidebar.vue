<template>
  <aside class="flex flex-col gap-5">
    <!-- Mon coin à moi -->
    <div>
      <h2 class="mb-3 text-[1.25rem] font-extrabold text-[#2d2a45]">Mon coin à moi</h2>

      <div class="rounded-[20px] border border-purple-100 bg-white p-4 shadow-sm">
        <div class="flex items-center gap-3">
          <span class="grid h-12 w-12 shrink-0 place-items-center rounded-full bg-[#f5efff] text-[1.7rem] leading-none">
            {{ apparence.avatar }}
          </span>
          <div class="min-w-0">
            <p class="truncate text-[1.05rem] font-extrabold text-[#2d2a45]">{{ apparence.avatarNom }}</p>
            <p class="text-[0.85rem] font-medium text-slate-400">C'est toi !</p>
          </div>
        </div>

        <button
          class="mt-4 w-full rounded-full border-[1.5px] border-[#7c3aed] bg-white py-2 text-[0.85rem] font-extrabold text-[#6d28d9] transition-colors hover:bg-purple-50"
          @click="$emit('personnaliser', 'profil')"
        >
          Personnaliser mon animal
        </button>

        <button
          class="mt-2 w-full rounded-full py-1.5 text-[0.75rem] font-bold text-slate-400 transition-colors hover:bg-slate-50 hover:text-purple-600"
          @click="$emit('personnaliser', 'themes')"
        >
          {{ themeActuel().emoji }} Changer le thème du jeu
        </button>
      </div>
    </div>

    <!-- Milo la mascotte -->
    <div class="rounded-[20px] bg-[#f2ecfa] p-4">
      <div class="relative rounded-2xl bg-white p-4 shadow-sm">
        <p class="text-[0.95rem] font-extrabold text-[#2d2a45]">Coucou, moi c'est Milo !</p>
        <p class="mt-0.5 text-[0.85rem] font-medium text-slate-600">
          Choisis un jeu et amuse-toi !
        </p>
        <!-- Petite pointe de la bulle vers Milo -->
        <span class="absolute -bottom-2 right-8 h-4 w-4 rotate-45 bg-white"></span>
      </div>

      <div class="mt-3 flex items-end justify-between gap-2">
        <p class="pb-2 text-[0.85rem] font-extrabold leading-snug text-[#6d28d9]">
          À chaque jeu,<br />une découverte !
        </p>
        <MascotMilo :taille="104" class="shrink-0 -rotate-2" />
      </div>
    </div>
  </aside>
</template>

<script setup>
import MascotMilo from './MascotMilo.vue'
import { apparence, themeActuel } from '../stores/apparence'

defineEmits(['personnaliser'])
</script>

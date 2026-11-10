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
            <input
              class="w-full rounded-xl border-2 border-transparent bg-transparent px-1 py-0.5 text-[1.05rem] font-extrabold text-[#2d2a45] transition-colors outline-none hover:border-purple-100 focus:border-purple-400"
              :value="progression.pseudo"
              maxlength="20"
              placeholder="Ton prénom"
              aria-label="Ton prénom"
              @change="changerNom"
            />
            <p class="px-1 text-[0.8rem] font-medium text-slate-400">
              {{ apparence.avatarNom }} — c'est toi ! Écris ton prénom ici.
            </p>
          </div>
        </div>

        <button
          class="mt-4 w-full rounded-full border-[1.5px] border-[#7c3aed] bg-white py-2 text-[0.85rem] font-extrabold text-[#6d28d9] transition-colors hover:bg-purple-50"
          @click="$emit('personnaliser', 'profil')"
        >
          Personnaliser mon animal
        </button>

        <!-- Thème actuel : petit autocollant de l'image + lien pour changer -->
        <div
          class="mt-3 flex items-center gap-3 rounded-2xl bg-[#f7f4fe] p-2.5"
          @click="$emit('personnaliser', 'themes')"
          role="button"
          tabindex="0"
        >
          <span
            class="h-12 w-12 shrink-0 rounded-xl border-[3px] border-white bg-cover bg-center shadow ring-1 ring-purple-100"
            :style="{ backgroundImage: themeActuel().image ? `url('${themeActuel().image}'), ${themeActuel().apercu}` : themeActuel().apercu }"
            aria-hidden="true"
          ></span>
          <span class="min-w-0 flex-1">
            <span class="block truncate text-[0.8rem] font-bold text-[#2d2a45]">
              {{ themeActuel().nom }}
            </span>
            <span class="block text-[0.72rem] font-semibold text-purple-600">
              Changer le thème du jeu
            </span>
          </span>
        </div>
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
import { progression, choisirPseudo } from '../stores/progression'

defineEmits(['personnaliser'])

function changerNom(evenement) {
  choisirPseudo(evenement.target.value)
  evenement.target.value = progression.pseudo
}
</script>

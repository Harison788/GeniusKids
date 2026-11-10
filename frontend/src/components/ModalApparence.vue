<template>
  <div
    class="fixed inset-0 z-50 flex items-start justify-center overflow-y-auto bg-slate-900/40 p-4 pt-10"
    @click.self="$emit('fermer')"
  >
    <div class="relative w-full max-w-lg rounded-3xl bg-white p-6 shadow-2xl">
      <button
        class="absolute right-4 top-4 grid h-9 w-9 place-items-center rounded-full bg-purple-50 font-extrabold text-purple-600 transition-colors hover:bg-purple-100"
        aria-label="Fermer"
        @click="$emit('fermer')"
      >
        ✕
      </button>

      <!-- Onglets -->
      <div class="mb-5 flex gap-2">
        <button
          v-for="o in ['profil', 'themes']"
          :key="o"
          class="flex-1 rounded-full py-2.5 text-sm font-extrabold transition-colors"
          :class="onglet === o ? 'bg-purple-700 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'"
          @click="onglet = o"
        >
          {{ o === 'profil' ? 'Mon profil' : 'Mes thèmes' }}
        </button>
      </div>

      <!-- Onglet profil : prénom + avatar -->
      <div v-if="onglet === 'profil'" class="flex flex-col gap-5">
        <div class="flex items-center gap-4 rounded-2xl bg-[#f3f0ff] p-4">
          <span class="grid h-14 w-14 shrink-0 place-items-center rounded-full bg-white text-3xl shadow-sm">
            {{ apparence.avatar }}
          </span>
          <div class="min-w-0 flex-1">
            <input
              class="w-full rounded-xl border-2 border-purple-200 px-3 py-2 font-bold text-slate-700 outline-none transition-colors focus:border-purple-500"
              :value="progression.pseudo"
              maxlength="20"
              aria-label="Ton prénom"
              @change="changerPseudo"
            />
            <p class="mt-1 text-sm font-bold text-slate-500">{{ apparence.avatarNom }}</p>
          </div>
        </div>

        <div v-for="groupe in AVATARS" :key="groupe.groupe">
          <p class="mb-2 text-sm font-extrabold text-purple-700">{{ groupe.groupe }}</p>
          <div class="grid grid-cols-6 gap-2 sm:grid-cols-7">
            <button
              v-for="avatar in groupe.liste"
              :key="avatar.emoji"
              class="grid aspect-square place-items-center rounded-2xl border-2 text-2xl transition-colors"
              :class="apparence.avatar === avatar.emoji
                ? 'border-purple-600 bg-white'
                : 'border-transparent bg-slate-50 hover:bg-purple-50'"
              :title="avatar.nom"
              @click="choisirAvatar(avatar)"
            >
              {{ avatar.emoji }}
            </button>
          </div>
        </div>
      </div>

      <!-- Onglet thèmes : le décor du jeu -->
      <div v-else class="flex flex-col gap-3">
        <p class="text-sm font-semibold text-slate-500">
          Le thème change les couleurs et le décor derrière les jeux.
          Le violet doux est celui de départ.
        </p>

        <button
          v-for="theme in THEMES"
          :key="theme.id"
          class="flex items-center gap-4 rounded-2xl border-2 p-3 text-left transition-colors"
          :class="apparence.theme === theme.id
            ? 'border-purple-600 bg-white'
            : 'border-transparent bg-slate-50 hover:bg-purple-50'"
          @click="choisirTheme(theme.id)"
        >
          <span
            class="grid h-12 w-12 shrink-0 place-items-center rounded-full text-2xl shadow-inner"
            :style="{ backgroundImage: theme.apercu }"
          >
            {{ theme.emoji }}
          </span>
          <span class="flex-1">
            <span class="block font-extrabold text-slate-800">{{ theme.nom }}</span>
            <span v-if="apparence.theme !== 'violet'" class="block text-xs font-semibold text-slate-400">
              Décor complet et coloré
            </span>
            <span v-else class="block text-xs font-semibold text-slate-400">
              Décor de la maquette
            </span>
          </span>
          <span v-if="apparence.theme === theme.id" class="text-sm font-extrabold text-purple-600">
            Choisi ✓
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { AVATARS, THEMES, apparence, choisirAvatar, choisirTheme } from '../stores/apparence'
import { progression, choisirPseudo, enregistrer } from '../stores/progression'

const props = defineProps({ ongletInitial: { type: String, default: 'profil' } })
defineEmits(['fermer'])

const onglet = ref(props.ongletInitial)

function changerPseudo(evenement) {
  choisirPseudo(evenement.target.value)
  evenement.target.value = progression.pseudo
  enregistrer()
}
</script>

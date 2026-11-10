<template>
  <svg :width="taille" :height="taille" viewBox="0 0 24 24" fill="none" aria-hidden="true">
    <rect x="2" y="7" width="20" height="12" rx="6" stroke="currentColor" stroke-width="2" />
    <path d="M7.5 11 V15 M5.5 13 H9.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
    <circle cx="15.5" cy="11.5" r="1.2" fill="currentColor" />
    <circle cx="17.8" cy="14" r="1.2" fill="currentColor" />
  </svg>
</template>

<script setup>
defineProps({ taille: { type: Number, default: 15 } })
</script>

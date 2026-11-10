<template>
  <svg :width="taille" :height="taille" viewBox="0 0 24 24" fill="none" aria-hidden="true">
    <path
      d="M3.5 10.5 L12 3.5 L20.5 10.5 M5.5 9 V19.5 H18.5 V9"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path d="M10 19.5 V14.5 H14 V19.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
  </svg>
</template>

<script setup>
defineProps({ taille: { type: Number, default: 15 } })
</script>

<template>
  <svg
    :width="taille"
    :height="taille"
    viewBox="0 0 100 100"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true"
  >
    <!-- Bras qui salue -->
    <path
      d="M78 38 C88 30 90 20 84 14"
      stroke="#7c5cff"
      stroke-width="9"
      stroke-linecap="round"
    />
    <!-- Corps -->
    <ellipse cx="48" cy="58" rx="34" ry="36" fill="#8b6cf7" />
    <ellipse cx="48" cy="66" rx="24" ry="24" fill="#f3f0ff" />
    <!-- Cornes -->
    <path d="M30 28 C26 18 30 12 36 12 C38 18 36 24 33 30 Z" fill="#6d4df0" />
    <path d="M66 28 C70 18 66 12 60 12 C58 18 60 24 63 30 Z" fill="#6d4df0" />
    <!-- Yeux -->
    <circle cx="38" cy="50" r="7.5" fill="#ffffff" />
    <circle cx="58" cy="50" r="7.5" fill="#ffffff" />
    <circle cx="39.5" cy="51" r="3.6" fill="#26244a" />
    <circle cx="56.5" cy="51" r="3.6" fill="#26244a" />
    <!-- Joues -->
    <circle cx="31" cy="62" r="4.5" fill="#c7b6ff" opacity="0.8" />
    <circle cx="65" cy="62" r="4.5" fill="#c7b6ff" opacity="0.8" />
    <!-- Sourire -->
    <path
      d="M41 62 Q48 70 55 62"
      stroke="#26244a"
      stroke-width="3"
      stroke-linecap="round"
      fill="none"
    />
    <!-- Pieds -->
    <ellipse cx="36" cy="93" rx="9" ry="4.5" fill="#6d4df0" />
    <ellipse cx="60" cy="93" rx="9" ry="4.5" fill="#6d4df0" />
  </svg>
</template>

<script setup>
defineProps({ taille: { type: Number, default: 96 } })
</script>

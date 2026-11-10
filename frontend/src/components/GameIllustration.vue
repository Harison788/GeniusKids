<template>
  <!-- Illustrations dessinées des jeux, fidèles à la maquette -->
  <svg
    viewBox="0 0 100 100"
    :width="taille"
    :height="taille"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true"
    class="mx-auto"
  >
    <!-- Quiz : deux tuiles calcul (+ et =) -->
    <template v-if="slug === 'quiz'">
      <circle cx="88" cy="14" r="5" fill="#a78bfa" />
      <g transform="rotate(-10 26 42)">
        <rect x="8" y="24" width="36" height="36" rx="10" fill="#8b5cf6" />
        <rect x="23" y="31" width="6" height="22" rx="3" fill="#ffffff" />
        <rect x="15" y="39" width="22" height="6" rx="3" fill="#ffffff" />
      </g>
      <g transform="rotate(8 66 60)">
        <rect x="48" y="42" width="36" height="36" rx="10" fill="#fbbf24" />
        <rect x="56" y="53" width="20" height="6" rx="3" fill="#ffffff" />
        <rect x="56" y="63" width="20" height="6" rx="3" fill="#ffffff" />
      </g>
    </template>

    <!-- Memory : deux cartes à jouer avec étoiles -->
    <template v-else-if="slug === 'memory'">
      <g transform="rotate(-14 30 50)">
        <rect x="10" y="22" width="36" height="48" rx="10" fill="#fbbf24" />
        <path d="M28 36 L31.5 46 L42 46 L33.5 52.5 L36.5 63 L28 56.5 L19.5 63 L22.5 52.5 L14 46 L24.5 46 Z" fill="#ffffff" />
      </g>
      <g transform="rotate(10 62 55)">
        <rect x="42" y="30" width="40" height="52" rx="10" fill="#8b5cf6" />
        <rect x="47" y="35" width="30" height="42" rx="7" fill="#ffffff" />
        <path d="M62 44 L65 53 L74.5 53 L66.7 58.8 L69.6 68 L62 62.2 L54.4 68 L57.3 58.8 L49.5 53 L59 53 Z" fill="#fbbf24" />
      </g>
    </template>

    <!-- Fusion des fruits : pomme + orange -->
    <template v-else-if="slug === 'fruits'">
      <circle cx="36" cy="58" r="26" fill="#ef5350" />
      <path d="M36 32 C36 24 40 20 46 18" stroke="#7a4b2a" stroke-width="5" stroke-linecap="round" />
      <path d="M44 24 C54 18 64 22 66 30 C56 36 46 32 44 24 Z" fill="#66bb6a" />
      <circle cx="27" cy="50" r="7" fill="#ff8a80" />
      <circle cx="70" cy="62" r="20" fill="#ffa726" />
      <circle cx="63" cy="55" r="5" fill="#ffcc80" />
      <path d="M70 42 C70 36 74 33 79 32" stroke="#7a4b2a" stroke-width="4" stroke-linecap="round" />
      <path d="M76 36 C84 32 91 35 92 41 C85 45 78 42 76 36 Z" fill="#66bb6a" />
    </template>

    <!-- Puzzles : pièces emboîtées -->
    <template v-else-if="slug === 'puzzle'">
      <g transform="rotate(-8 35 45)">
        <rect x="14" y="26" width="34" height="34" rx="6" fill="#8b5cf6" />
        <circle cx="48" cy="43" r="8" fill="#8b5cf6" />
        <circle cx="31" cy="26" r="8" fill="#8b5cf6" />
      </g>
      <g transform="rotate(10 62 62)">
        <rect x="44" y="44" width="34" height="34" rx="6" fill="#fbbf24" />
        <circle cx="61" cy="44" r="8" fill="#fbbf24" />
        <rect x="74" y="55" width="12" height="8" rx="4" fill="#34d399" />
      </g>
      <circle cx="14" cy="20" r="4" fill="#34d399" />
    </template>

    <!-- Kakuro : grille de calcul -->
    <template v-else-if="slug === 'kakuro'">
      <rect x="14" y="18" width="30" height="30" rx="7" fill="#c4b5fd" />
      <rect x="50" y="18" width="30" height="30" rx="7" fill="#ede9fe" />
      <rect x="14" y="54" width="30" height="30" rx="7" fill="#8b5cf6" />
      <rect x="50" y="54" width="30" height="30" rx="7" fill="#ffffff" stroke="#c4b5fd" stroke-width="3" />
      <circle cx="29" cy="33" r="4" fill="#ffffff" />
      <circle cx="65" cy="33" r="4" fill="#8b5cf6" />
      <circle cx="29" cy="69" r="4" fill="#ffffff" />
      <circle cx="65" cy="69" r="4" fill="#8b5cf6" />
    </template>

    <!-- Comptage : boulier -->
    <template v-else-if="slug === 'comptage'">
      <rect x="12" y="14" width="8" height="74" rx="4" fill="#8b5cf6" />
      <rect x="80" y="14" width="8" height="74" rx="4" fill="#8b5cf6" />
      <rect x="14" y="26" width="72" height="6" rx="3" fill="#c4b5fd" />
      <rect x="14" y="50" width="72" height="6" rx="3" fill="#c4b5fd" />
      <rect x="14" y="74" width="72" height="6" rx="3" fill="#c4b5fd" />
      <circle cx="28" cy="29" r="8" fill="#fb923c" />
      <circle cx="46" cy="29" r="8" fill="#fb923c" />
      <circle cx="64" cy="29" r="8" fill="#ef5350" />
      <circle cx="34" cy="53" r="8" fill="#ef5350" />
      <circle cx="52" cy="53" r="8" fill="#fbbf24" />
      <circle cx="70" cy="53" r="8" fill="#fbbf24" />
      <circle cx="28" cy="77" r="8" fill="#34d399" />
      <circle cx="46" cy="77" r="8" fill="#34d399" />
      <circle cx="64" cy="77" r="8" fill="#8b5cf6" />
    </template>

    <!-- Repli générique : dé -->
    <template v-else>
      <rect x="20" y="20" width="60" height="60" rx="14" fill="#8b5cf6" />
      <circle cx="40" cy="40" r="6" fill="#ffffff" />
      <circle cx="60" cy="60" r="6" fill="#ffffff" />
    </template>
  </svg>
</template>

<script setup>
defineProps({
  slug: { type: String, required: true },
  taille: { type: Number, default: 84 },
})
</script>

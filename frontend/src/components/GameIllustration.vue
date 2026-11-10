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

    <!-- Memory : carte violette à étoile + carte blanche à étoile dorée -->
    <template v-else-if="slug === 'memory'">
      <g transform="rotate(-14 30 55)">
        <rect x="12" y="26" width="40" height="52" rx="10" fill="#8b5cf6" />
        <path d="M32 40 L35.5 50 L46 50 L37.5 56.5 L40.5 67 L32 60.5 L23.5 67 L26.5 56.5 L18 50 L28.5 50 Z" fill="#ffffff" />
      </g>
      <g transform="rotate(10 64 52)">
        <rect x="44" y="20" width="40" height="52" rx="10" fill="#ffffff" stroke="#e9e4fb" stroke-width="3" />
        <path d="M64 34 L67.3 44 L78 44 L69.5 50.5 L72.6 61 L64 54.7 L55.4 61 L58.5 50.5 L50 44 L60.7 44 Z" fill="#fbbf24" />
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

    <!-- Kakuro : mini-grille avec cases violettes et pastille dorée -->
    <template v-else-if="slug === 'kakuro'">
      <circle cx="86" cy="12" r="4" fill="#c4b5fd" />
      <rect x="14" y="18" width="32" height="32" rx="8" fill="#c4b5fd" />
      <path d="M18 44 L42 24" stroke="#ffffff" stroke-width="4" stroke-linecap="round" />
      <rect x="54" y="18" width="32" height="32" rx="8" fill="#ffffff" stroke="#ddd5fa" stroke-width="3" />
      <rect x="14" y="56" width="32" height="32" rx="8" fill="#8b5cf6" />
      <circle cx="30" cy="72" r="5" fill="#ffffff" />
      <rect x="54" y="56" width="32" height="32" rx="8" fill="#ffffff" stroke="#ddd5fa" stroke-width="3" />
      <circle cx="70" cy="66" r="5" fill="#fbbf24" />
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

    <!-- Piano : clavier avec touches blanches et noires -->
    <template v-else-if="slug === 'piano'">
      <rect x="10" y="10" width="80" height="18" rx="9" fill="#c084fc" opacity="0.6" />
      <g v-for="(x, i) in [14, 30, 46, 62, 78]" :key="x">
        <rect :x="x" y="38" width="14" height="46" rx="4" fill="#ffffff" stroke="#d8cef5" stroke-width="2.5" />
      </g>
      <rect x="23.5" y="38" width="9" height="26" rx="3" fill="#3b2a6b" />
      <rect x="39.5" y="38" width="9" height="26" rx="3" fill="#3b2a6b" />
      <circle cx="55" cy="73" r="5" fill="#fbbf24" />
      <rect x="69.5" y="38" width="9" height="26" rx="3" fill="#3b2a6b" />
    </template>

    <!-- Échecs : échiquier + tour violette et pion doré -->
    <template v-else-if="slug === 'echecs'">
      <g>
        <rect x="12" y="34" width="18" height="18" rx="3" fill="#ddd6fe" />
        <rect x="30" y="34" width="18" height="18" rx="3" fill="#ffffff" stroke="#c4b5fd" stroke-width="2" />
        <rect x="48" y="34" width="18" height="18" rx="3" fill="#ddd6fe" />
        <rect x="66" y="34" width="18" height="18" rx="3" fill="#ffffff" stroke="#c4b5fd" stroke-width="2" />
        <rect x="12" y="52" width="18" height="18" rx="3" fill="#ffffff" stroke="#c4b5fd" stroke-width="2" />
        <rect x="30" y="52" width="18" height="18" rx="3" fill="#ddd6fe" />
        <rect x="48" y="52" width="18" height="18" rx="3" fill="#ffffff" stroke="#c4b5fd" stroke-width="2" />
        <rect x="66" y="52" width="18" height="18" rx="3" fill="#ddd6fe" />
        <rect x="12" y="70" width="18" height="18" rx="3" fill="#ddd6fe" />
        <rect x="30" y="70" width="18" height="18" rx="3" fill="#ffffff" stroke="#c4b5fd" stroke-width="2" />
        <rect x="48" y="70" width="18" height="18" rx="3" fill="#ddd6fe" />
        <rect x="66" y="70" width="18" height="18" rx="3" fill="#ffffff" stroke="#c4b5fd" stroke-width="2" />
      </g>
      <!-- Tour violette posée sur une case -->
      <g transform="translate(13, 33)">
        <path d="M8 0 L24 0 L24 6 L20 8.5 L20 14 L12 14 L12 8.5 L8 6 Z" fill="#7c3aed" />
        <rect x="5" y="14" width="22" height="5" rx="2.5" fill="#7c3aed" />
      </g>
      <!-- Pion doré -->
      <g transform="translate(65, 56)">
        <circle cx="15" cy="9" r="8" fill="#fbbf24" />
        <path d="M6 30 L6 25 Q15 18 24 25 L24 30 Z" fill="#fbbf24" />
        <rect x="5" y="29" width="20" height="5" rx="2.5" fill="#f59e0b" />
      </g>
      <circle cx="90" cy="12" r="4" fill="#a78bfa" />
    </template>

    <!-- Sudoku : grille 2x2 avec chiffres -->
    <template v-else-if="slug === 'sudoku'">
      <rect x="14" y="24" width="72" height="72" rx="10" fill="#ffffff" stroke="#a7d9b8" stroke-width="3.5" />
      <line x1="50" y1="24" x2="50" y2="96" stroke="#a7d9b8" stroke-width="2.5" />
      <line x1="14" y1="60" x2="86" y2="60" stroke="#a7d9b8" stroke-width="2.5" />
      <rect x="30" y="38" width="14" height="14" rx="4" fill="#dcf3e3" />
      <rect x="60" y="72" width="14" height="14" rx="4" fill="#dcf3e3" />
      <text x="43" y="70" font-size="26" font-weight="bold" fill="#166534" font-family="Segoe UI, sans-serif" text-anchor="middle">1</text>
      <text x="70" y="54" font-size="26" font-weight="bold" fill="#166534" font-family="Segoe UI, sans-serif" text-anchor="middle">4</text>
      <circle cx="92" cy="18" r="4" fill="#34d399" />
    </template>

    <!-- Mots croisés : cases avec lettres -->
    <template v-else-if="slug === 'mots'">
      <g v-for="(x, i) in [18, 42, 66]" :key="x">
        <rect :x="x" y="26" width="20" height="20" rx="4" fill="#ffffff" stroke="#e8d48a" stroke-width="2.5" />
      </g>
      <rect x="18" y="50" width="20" height="20" rx="4" fill="#fdf0cc" />
      <rect x="42" y="50" width="20" height="20" rx="4" fill="#ffffff" stroke="#e8d48a" stroke-width="2.5" />
      <rect x="66" y="50" width="20" height="20" rx="4" fill="#fdf0cc" />
      <text x="52" y="66" font-size="17" font-weight="bold" fill="#a16207" font-family="Segoe UI, sans-serif" text-anchor="middle">A</text>
      <text x="28" y="43" font-size="17" font-weight="bold" fill="#a16207" font-family="Segoe UI, sans-serif" text-anchor="middle">C</text>
      <circle cx="90" cy="14" r="5" fill="#fbbf24" />
      <rect x="18" y="74" width="20" height="20" rx="4" fill="#ffffff" stroke="#e8d48a" stroke-width="2.5" />
    </template>

    <!-- Langue : bulles de parole FR / EN -->
    <template v-else-if="slug === 'langue'">
      <circle cx="40" cy="40" r="26" fill="#8b5cf6" />
      <path d="M32 64 L28 76 L42 66 Z" fill="#8b5cf6" />
      <text x="40" y="47" font-size="19" font-weight="bold" fill="#ffffff" font-family="Segoe UI, sans-serif" text-anchor="middle">FR</text>
      <circle cx="68" cy="58" r="22" fill="#fbbf24" />
      <path d="M76 78 L82 88 L68 80 Z" fill="#fbbf24" />
      <text x="68" y="65" font-size="16" font-weight="bold" fill="#7c4a03" font-family="Segoe UI, sans-serif" text-anchor="middle">EN</text>
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

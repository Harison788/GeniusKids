# GeniusKids

Application de jeux de mathématiques pour les enfants de **4 à 11 ans**, construite avec **Django** (API) et **Vue.js 3** (interface). Installable sur mobile en tant que PWA.

## Jeux inclus

| Jeu | Description |
|---|---|
| ➕ Quiz de Maths | Calcul avec choix multiples, feedback immédiat |
| 🔢 Comptage | Compter les objets et compléter les suites |
| 🃏 Memory | Retourner les cartes et trouver les paires (calcul ↔ résultat) |
| 🔗 Associations | Relier les cartes qui vont ensemble (thèmes variés) |
| 🧊 Kakuro | Lignes et colonnes doivent atteindre la somme indiquée |
| ✏️ Relie les Points | Suivre les numéros pour dessiner la forme secrète |
| 🍓 Fusion des Fruits | Deux fruits identiques fusionnent : fraise → pastèque |
| 🧩 Puzzle | Échanger les pièces pour recomposer le dessin |

3 niveaux selon l'âge : 🐿️ Écureuil (4-6 ans), 🦊 Renard (6-8 ans), 🦉 Hibou (9-11 ans).
La progression (pseudo, étoiles, records) est enregistrée localement dans le navigateur — **sans inscription**.

## Structure

```
kids-games/
├── backend/        # Django + DRF : génération des jeux + scores
│   ├── config/     # Réglages du projet
│   └── games/      # API (vues, modèles, serializers)
└── frontend/       # Vue 3 + Vite : l'interface enfant
    └── src/        # Composants, vues, styles, PWA
```

## Démarrage (développement)

### 1. Backend (terminal 1)

```powershell
cd kids-games\backend
venv\Scripts\Activate.ps1          # Windows PowerShell
python manage.py migrate           # première fois seulement
python manage.py runserver         # → http://127.0.0.1:8000
```

### 2. Frontend (terminal 2)

```powershell
cd kids-games\frontend
npm run dev                        # → http://localhost:5173
```

L'interface est disponible sur **http://localhost:5173** (les appels `/api/*` sont proxifiés vers Django).

## API

| Route | Description |
|---|---|
| `GET /api/quiz/?niveau=1..3` | Questions de calcul avec choix |
| `GET /api/comptage/?niveau=1..3` | Questions de comptage / suites |
| `GET /api/memory/?niveau=1..3` | Deck de 6 paires de cartes |
| `GET /api/associations/?niveau=1..3` | Un thème + 4 paires à relier |
| `GET /api/kakuro/?niveau=1..3` | Grille de sommes (cible lignes/colonnes + solution) |
| `GET /api/scores/?pseudo=…` | Meilleurs scores (optionnel) |
| `POST /api/scores/` | Enregistrer un score |

## 📱 Sur mobile

L'interface est **responsive** et l'app est une **PWA** : visitée une fois depuis le navigateur du téléphone (même réseau Wi-Fi), elle peut être installée via « Ajouter à l'écran d'accueil » et se lance comme une vraie application.

Mise en boutique (Play Store / App Store) : voir l'étape **Capacitor** documentée à suivre.

/* Progression simple, sans inscription : gardée dans le navigateur
   et synchronisée avec le profil Django (UserProfile). */
import { reactive } from 'vue'
import API from '../api'

const CLE = 'geniuskids-progression'

function vide() {
  return { pseudo: 'Petit curieux', niveau: 1, etoiles: 0, meilleures: {} }
}

function charger() {
  try {
    const brut = JSON.parse(localStorage.getItem(CLE))
    return brut && typeof brut === 'object' ? { ...vide(), ...brut } : vide()
  } catch {
    return vide()
  }
}

export const progression = reactive(charger())

export function enregistrer() {
  try {
    localStorage.setItem(CLE, JSON.stringify(progression))
  } catch {
    // Stockage indisponible (mode privé) : on continue sans sauvegarde.
  }
}

/* Envoie nom + étoiles au profil Django (sans bloquer l'interface). */
function synchroniserProfil() {
  API.majProfil({ nom: progression.pseudo, etoiles: progression.etoiles })
}

/* Récupère le profil distant (étoiles gagnées sur un autre appareil, etc.). */
export async function chargerProgressionDistante() {
  try {
    const profil = await API.chargerProfil()
    if (profil.nom && profil.nom !== 'Petit curieux') progression.pseudo = profil.nom
    if (profil.etoiles > progression.etoiles) progression.etoiles = profil.etoiles
    enregistrer()
    return profil
  } catch {
    return null
  }
}

export function ajouterEtoiles(nombre) {
  progression.etoiles += nombre
  enregistrer()
  synchroniserProfil()
}

export function meilleure(jeu) {
  return progression.meilleures[`${jeu}-${progression.niveau}`] ?? null
}

export function noterScore(jeu, niveau, points, etoiles) {
  const cle = `${jeu}-${niveau}`
  const existe = progression.meilleures[cle]
  if (!existe || points > existe.points) {
    progression.meilleures[cle] = { points, etoiles, date: new Date().toISOString() }
  }
  progression.etoiles += etoiles
  enregistrer()
  synchroniserProfil()
}

export function choisirPseudo(pseudo) {
  progression.pseudo = (pseudo || '').trim().slice(0, 20) || 'Petit curieux'
  enregistrer()
  synchroniserProfil()
}

export function choisirNiveau(niveau) {
  progression.niveau = niveau
  enregistrer()
}

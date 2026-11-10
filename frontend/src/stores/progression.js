/* Progression simple, sans inscription : tout est gardé dans le navigateur. */
import { reactive } from 'vue'

const CLE = 'petits-genies-progression'

function vide() {
  return { pseudo: 'Agent mystère', niveau: 1, etoiles: 0, meilleures: {} }
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

export function ajouterEtoiles(nombre) {
  progression.etoiles += nombre
  enregistrer()
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
}

export function choisirPseudo(pseudo) {
  progression.pseudo = (pseudo || '').trim().slice(0, 20) || 'Agent mystère'
  enregistrer()
}

export function choisirNiveau(niveau) {
  progression.niveau = niveau
  enregistrer()
}

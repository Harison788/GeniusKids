/* Service worker PWA : réseau d'abord, cache en secours hors ligne.
   La version du cache change à chaque renouvellement important pour purger l'ancien. */
const CACHE = 'petits-curieux-v3'

self.addEventListener('install', () => self.skipWaiting())

self.addEventListener('activate', (evenement) => {
  evenement.waitUntil(
    (async () => {
      const noms = await caches.keys()
      await Promise.all(noms.filter((nom) => nom !== CACHE).map((nom) => caches.delete(nom)))
      await clients.claim()
    })(),
  )
})

self.addEventListener('fetch', (evenement) => {
  if (evenement.request.method !== 'GET') return

  const url = new URL(evenement.request.url)
  const navigation = evenement.request.mode === 'navigate' || url.pathname === '/'

  evenement.respondWith(
    (async () => {
      try {
        // Toujours le réseau d'abord : le cache sert seulement hors ligne.
        const reseau = await fetch(evenement.request)
        if (reseau.ok && reponseCompatible(reseau)) {
          const copie = reseau.clone()
          caches.open(CACHE).then((cache) => cache.put(evenement.request, copie))
        }
        return reseau
      } catch {
        const cache = await caches.open(CACHE)
        const enCache = await cache.match(evenement.request)
        if (enCache) return enCache
        if (navigation) {
          const accueil = await cache.match('/')
          if (accueil) return accueil
        }
        throw new Error('hors ligne')
      }
    })(),
  )
})

function reponseCompatible(reponse) {
  return reponse.type === 'basic' || reponse.type === 'cors'
}

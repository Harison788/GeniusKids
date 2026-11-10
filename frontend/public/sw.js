/* Service worker minimal : cache à l'exécution pour l'installation PWA. */
const CACHE = 'petits-genies-v1'

self.addEventListener('install', () => self.skipWaiting())

self.addEventListener('activate', (evenement) => {
  evenement.waitUntil(clients.claim())
})

self.addEventListener('fetch', (evenement) => {
  if (evenement.request.method !== 'GET') return
  evenement.respondWith(
    caches.match(evenement.request).then((enCache) => {
      if (enCache) return enCache
      return fetch(evenement.request).then((reponse) => {
        if (reponse.ok && reponse.type === 'basic') {
          const copie = reponse.clone()
          caches.open(CACHE).then((cache) => cache.put(evenement.request, copie))
        }
        return reponse
      }).catch(() => enCache)
    })
  )
})

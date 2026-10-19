/* Network-first service worker: always tries the live site, falls back to the cache when offline. */
const CACHE = 'mced-v1';
self.addEventListener('install', e => { self.skipWaiting() });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(k => Promise.all(k.filter(x => x !== CACHE).map(x => caches.delete(x)))).then(() => self.clients.claim())) });
self.addEventListener('fetch', e => {
    const r = e.request; if (r.method !== 'GET' || !r.url.startsWith(self.location.origin) || r.url.includes('/api/')) return;
    e.respondWith(fetch(r).then(res => { const c = res.clone(); caches.open(CACHE).then(ch => ch.put(r, c)); return res }).catch(() => caches.match(r).then(m => m || caches.match('index.html'))))
});

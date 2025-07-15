const cacheName = "offline-app-v1";
const assets = [
  "/",
  "/index.html",
  "/style.css",
  "/script.js"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(cacheName).then((cache) => {
      return cache.addAll(assets);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request);
    }).catch(() => {
      return caches.match("/index.html"); // fallback if everything fails
    })
  );
});

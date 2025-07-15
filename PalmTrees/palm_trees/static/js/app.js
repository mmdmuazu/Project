setInterval(window.addEventListener("load", () => {
  document.getElementById("loader").style.display = "block";
}), 2000)
AOS.init();


function getId(id) {
  resp = document.getElementById(id);
  return resp;
}
function showLoader() {
  const loader = document.getElementById("loader");
  if (loader) loader.style.display = "flex";
}

function hideLoader() {
  const loader = document.getElementById("loader");
  if (loader) loader.style.display = "none";
}

// Hide loader on normal load
window.onload = hideLoader;

// Hide loader when navigating back (from cache)
window.addEventListener("pageshow", function (event) {
  hideLoader();
});

document.getElementById("menu-toggle").onclick = function () {
  document.getElementById("nav-links").classList.toggle("active");
};

function remove(){
  document.getElementById("nav-links").classList.remove('active');
  // return;
}


function addToCart(id, name, price, discount) {
  const finalPrice = price - (price * discount) / 100;
  const item = { id, name, price: finalPrice };
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  if (!cart.find((p) => p.id === id)) cart.push(item);
  localStorage.setItem("cart", JSON.stringify(cart));
  alert(`${name} added to cart!`);
}

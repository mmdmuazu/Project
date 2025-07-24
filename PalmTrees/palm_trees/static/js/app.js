setInterval(window.addEventListener("load", () => {
  document.getElementById("loader").style.display = "none";
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

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}



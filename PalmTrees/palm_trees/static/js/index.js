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
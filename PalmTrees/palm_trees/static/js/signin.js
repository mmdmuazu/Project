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
const login_form = document.querySelector("form");
const url = document.querySelector("input[name='login-url']").value;
const csrfToken = document.querySelector(
  "input[name='csrfmiddlewaretoken']"
).value;
const message = document.getElementById("message");
login_form.addEventListener("submit", (event) => {
  event.preventDefault();
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ username: "amir", password: 122334 }),
  })
    .then((resp) => resp.json())
    .then((data) => {
      message.textContent = JSON.stringify(data);
    })
    .catch((error) => {
      message.textContent = `please check you internet connection`;
    });
});

const getId = (id) => document.getElementById(id);
const fullNameField = getId("fullName");
const emailField = getId("email");
const passwordField = getId("password");
const confirmPasswordField = getId("confirmPassword");
const passwordMessage = getId("password-message");
const fullNameMessage = getId("fullName-message");
const emailMessage = getId("email-message");
const confirmPasswordMessage = getId("confirmPassword-message");
const message = getId("message");

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
const timeOut = (id, time) =>
  setTimeout((event) => {
    getId(id).textContent = "";
  }, time);
const myForm = getId("form");
myForm.addEventListener("submit", (event) => {
  event.preventDefault();
  showLoader();
  const url = document.querySelector("input[name='register-url']").value;
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": document.querySelector("input[name=csrfmiddlewaretoken]")
        .value,
    },
    body: JSON.stringify({
      fullName: fullNameField.value,
      email: emailField.value,
      password: passwordField.value,
      confirmPassword: confirmPasswordField.value,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data) {
        hideLoader();
      }
      if (data.success) {
        message.textContent = data.message;
        message.style.color = "green";
        timeOut("message", 2000);
      } else if (data.fullName) {
        fullNameMessage.textContent = data.fullName;
        fullNameField.style.border = "2px solid red";
        timeOut("fullName-message", 2000);
      } else if (data.email) {
        emailMessage.textContent = data.email;
      } else if (data.password) {
        console.log("password");
      } else if (data.confirmPassword) {
        confirmPasswordMessage.textContent = data.confirmPassword;
        confirmPasswordField.style.border = "2px solid red";
        timeOut("confirmPassword-message", 2000);
      } else {
        console.log("nothing");
      }
    })
    .catch((error) => {
      hideLoader();
      message.textContent = "Check your internet connection";
      timeOut("message", 2000);
    });
});

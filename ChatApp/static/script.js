const usernameSpan = document.getElementById("username");
const input = document.getElementById("nameInput");
const form = document.getElementById("usernameForm");

const loadUsername = () => {
  // Load from localStorage first
  const localUsername = localStorage.getItem("username");
  if (localUsername) {
    usernameSpan.textContent = localUsername;
  }

  // Try updating from server if online
  if (navigator.onLine) {
    fetch("/get_data")
      .then(res => res.json())
      .then(data => {
        if (data.username) {
          localStorage.setItem("username", data.username);
          usernameSpan.textContent = data.username;
        }
      })
      .catch(() => console.log("Server not reachable"));
  }
};

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const username = input.value.trim();
  if (!username) return;

  // Save locally
  localStorage.setItem("username", username);
  usernameSpan.textContent = username;

  // Send to server if online
  if (navigator.onLine) {
    await fetch("/update_username", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username })
    });
  }
});

loadUsername();

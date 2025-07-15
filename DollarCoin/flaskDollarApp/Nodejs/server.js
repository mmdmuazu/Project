const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3000;
const USERS_FILE = './users.json';

app.use(express.static('public'));

app.get('/api/user/:id', (req, res) => {
  const users = JSON.parse(fs.readFileSync(USERS_FILE));
  const user = users[req.params.id];
  if (user) {
    res.json(user);
  } else {
    res.status(404).json({ error: "User not found" });
  }
});

app.listen(PORT, () => {
  console.log(`🌍 API server running on http://localhost:${PORT}`);
});

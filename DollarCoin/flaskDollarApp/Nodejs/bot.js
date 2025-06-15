const TelegramBot = require('node-telegram-bot-api');
const fs = require('fs');
const token = '7424542157:AAE0-u3H_tc4ReJ1Ju9Zij9GrZ-FW08lv2A';
const bot = new TelegramBot(token, { polling: true });

const USERS_FILE = './users.json';
let users = fs.existsSync(USERS_FILE) ? JSON.parse(fs.readFileSync(USERS_FILE)) : {};

function saveUsers() {
  fs.writeFileSync(USERS_FILE, JSON.stringify(users, null, 2));
}

bot.onText(/\/start(?:\s+(\d+))?/, (msg, match) => {
  const chatId = msg.chat.id;
  const userId = msg.from.id.toString();
  const referrerId = match[1];

  if (!users[userId]) {
    users[userId] = {
      id: userId,
      name: msg.from.first_name,
      referredBy: referrerId || null,
      balance: 0
    };
    saveUsers();
    console.log(`✅ New user added: ${userId}`);
  }

  bot.sendMessage(chatId, `👋 Welcome ${msg.from.first_name}!`, {
    reply_markup: {
      inline_keyboard: [
        [{ text: "⛏️ Start Mining", callback_data: "mine" }],
        [{ text: "💰 Check Balance", callback_data: "balance" }]
      ]
    }
  });
});

bot.on('callback_query', (query) => {
  const chatId = query.message.chat.id;
  const userId = query.from.id.toString();
  const action = query.data;

  if (action === 'mine') {
    users[userId].balance += 1;
    saveUsers();
    bot.sendMessage(chatId, `⛏️ Mining... You earned 1 coin!`);
  } else if (action === 'balance') {
    const balance = users[userId].balance;
    bot.sendMessage(chatId, `💰 Your balance is: ${balance} coins`);
  }
});

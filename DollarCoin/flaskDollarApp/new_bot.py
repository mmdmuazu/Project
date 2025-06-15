from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json, os

TOKEN = "7424542157:AAE0-u3H_tc4ReJ1Ju9Zij9GrZ-FW081v2A"
WEBAPP_URL = "https://dollar.pythonanywhere.com"  # <-- REPLACE THIS

USER_FILE = "users.json"

def load_users():
    return json.load(open(USER_FILE)) if os.path.exists(USER_FILE) else {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)

users = load_users()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    name = update.effective_user.first_name

    # Save new user
    if user_id not in users:
        users[user_id] = {
            "id": user_id,
            "name": name,
            "balance": 0
        }
        save_users(users)

    keyboard = [
        [InlineKeyboardButton("🚀 Open Mining App", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    await update.message.reply_text(
        f"👋 Welcome {name}! Click below to open the app.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Telegram bot is running...")
app.run_polling()

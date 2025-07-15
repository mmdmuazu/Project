from telegram import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

print('/start clicked')


async def start(update, context):
    image_path = 'coin.png'
    user = update.effective_user
    username = update.message.from_user.username
    chat = update.message.chat_id
    print(chat)
    print(user.first_name)
    message_text = update.message.text or ""
    parts = message_text.split()
    referral_code = parts[1] if len(parts) > 1 else None
    print(f"Received the referral code: {referral_code}")

    # Create an InlineKeyboardButton with a URL
    play_button = WebAppInfo(url=f"https://dollar.pythonanywhere.com")
    telegram_button = InlineKeyboardButton("Join our community", url="https://t.me/dollar_coin_channel")
    twitter_button = InlineKeyboardButton("follow us on X", url="https://x.com/Dollarcoin32536?t=Gt4UETs7z0mmJppG6-rVLQ&s=0")

    # Create an InlineKeyboardMarkup with the button
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Play 🎮", web_app=play_button)], [telegram_button], [twitter_button]])



    # Send a message with the button
    with open(image_path, 'rb') as image_file:
        await update.message.reply_photo(photo=image_file, caption=f'Hi @{username}, tap on the coin and see your balance rise. DollarCoin is a decentralized exchange on the blockchain.', reply_markup=reply_markup)

# Initialize the Application
application = Application.builder().token("7424542157:AAE0-u3H_tc4ReJ1Ju9Zij9GrZ-FW08lv2A").build()

# Add a handler for the /start command
application.add_handler(CommandHandler("start", start))

# Start the bot
application.run_polling()

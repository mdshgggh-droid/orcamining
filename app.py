import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)
bot = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Welcome to BD Trusted Task!")

bot.add_handler(CommandHandler("start", start))

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    import threading
    threading.Thread(
        target=lambda: bot.run_polling(),
        daemon=True
    ).start()

    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "10000"))
    )

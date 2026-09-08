import os
import threading
import logging

from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("START COMMAND RECEIVED")
    await update.message.reply_text("✅ Welcome to BD Trusted Task!")


async def run_bot():
    try:
        if not TOKEN:
            print("❌ ERROR: BOT_TOKEN is missing!")
            return

        print("🔄 Starting Telegram Bot...")

        bot = Application.builder().token(TOKEN).build()

        bot.add_handler(CommandHandler("start", start))

        print("✅ Bot application created")
        print("🔄 Starting polling...")

        await bot.initialize()

        me = await bot.bot.get_me()
        print(f"✅ BOT CONNECTED: @{me.username}")

        await bot.start()
        await bot.updater.start_polling()

        print("✅ POLLING IS RUNNING")

        # Keep bot running
        import asyncio
        while True:
            await asyncio.sleep(3600)

    except Exception as e:
        print("❌ BOT ERROR:", repr(e))


def bot_thread():
    import asyncio
    asyncio.run(run_bot())


@app.route("/")
def home():
    return "Bot is running"


if __name__ == "__main__":
    threading.Thread(
        target=bot_thread,
        daemon=True
    ).start()

    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "10000"))
    )

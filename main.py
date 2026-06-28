from flask import Flask
from threading import Thread
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from market import get_price

TOKEN = os.environ.get("TOKEN")

web = Flask(__name__)

@web.route("/")
def home():
    return "Trading Bot is Running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Trading Bot Working Successfully!\n\n"
        "Commands:\n"
        "/price BTCUSDT\n"
        "/price ETHUSDT"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Usage:\n/price BTCUSDT")
        return

    symbol = context.args[0].upper()

    p = get_price(symbol)

    if p is None:
        await update.message.reply_text("❌ Invalid Coin Symbol")
    else:
        await update.message.reply_text(
            f"💰 {symbol}\n\nCurrent Price: {p} USDT"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    print("Bot Started...")

    Thread(target=run_web, daemon=True).start()

    app.run_polling()

if __name__ == "__main__":
    main()

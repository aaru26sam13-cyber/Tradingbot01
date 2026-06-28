import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ⚠️ Render मध्ये env variable आहे असं गृहित धरतो
BOT_TOKEN = os.getenv("8793772063:AAHgvP6G_Rdy3bnCKnFmfhMsxdNB-ApqY6U")


def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        return requests.get(url, timeout=10).json()["price"]
    except:
        return None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Ready 🤖")


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("/price BTCUSDT")
        return

    symbol = context.args[0].upper()
    p = get_price(symbol)

    if p:
        await update.message.reply_text(f"{symbol}: {p}")
    else:
        await update.message.reply_text("Invalid Symbol")


def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN missing in Render Environment")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    print("Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()

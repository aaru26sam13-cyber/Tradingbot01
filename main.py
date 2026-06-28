import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Environment Token (SAFE CHECK)
BOT_TOKEN = os.getenv("BOT_TOKEN")


# 💰 Price
def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        r = requests.get(url, timeout=10)
        return r.json()["price"]
    except:
        return None


# 📊 Signal
def get_signal(symbol):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        change = float(data["priceChangePercent"])

        if change > 2:
            return "🟢 BUY"
        elif change < -2:
            return "🔴 SELL"
        else:
            return "🟡 HOLD"
    except:
        return "❌ Error"


# 🚀 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Started!\n\n"
        "/price BTCUSDT\n"
        "/signal BTCUSDT"
    )


# 💰 PRICE
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /price BTCUSDT")
        return

    symbol = context.args[0].upper()
    result = get_price(symbol)

    if result:
        await update.message.reply_text(f"💰 {symbol}: {result}")
    else:
        await update.message.reply_text("❌ Invalid Symbol")


# 📊 SIGNAL
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /signal BTCUSDT")
        return

    symbol = context.args[0].upper()
    result = get_signal(symbol)

    await update.message.reply_text(f"📊 {symbol}: {result}")


# 🔥 MAIN (SAFE ENV CHECK ADDED)
def main():
    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN missing in Environment Variables (Render)")
        print("👉 Go to Render → Environment → Add BOT_TOKEN")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("signal", signal))

    print("🤖 Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()

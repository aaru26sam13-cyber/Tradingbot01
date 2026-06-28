import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Render/GitHub Environment Token
BOT_TOKEN = os.getenv("BOT_TOKEN")


# 💰 Binance Price
def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        return data["price"]
    except:
        return None


# 📊 Simple Signal Logic
def get_signal(symbol):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()

        change = float(data["priceChangePercent"])

        if change > 2:
            return "🟢 BUY (Strong Uptrend)"
        elif change < -2:
            return "🔴 SELL (Downtrend)"
        else:
            return "🟡 HOLD (Sideways Market)"
    except:
        return "❌ Error fetching signal"


# 🚀 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Started Successfully!\n\n"
        "Commands:\n"
        "/price BTCUSDT\n"
        "/signal BTCUSDT"
    )


# 💰 /price
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Usage: /price BTCUSDT")
        return

    symbol = context.args[0].upper()
    price = get_price(symbol)

    if price:
        await update.message.reply_text(f"💰 {symbol} Price: {price}")
    else:
        await update.message.reply_text("❌ Invalid Symbol")


# 📊 /signal
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Usage: /signal BTCUSDT")
        return

    symbol = context.args[0].upper()
    result = get_signal(symbol)

    await update.message.reply_text(f"📊 {symbol}\n{result}")


# 🔥 Main Function
def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN not found in environment variables")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("signal", signal))

    print("🤖 Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()

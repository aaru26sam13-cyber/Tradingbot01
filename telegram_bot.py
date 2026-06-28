from telegram.ext import Updater, CommandHandler
import requests

TOKEN = "YOUR_BOT_TOKEN"


# 📊 Get price from Binance
def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    r = requests.get(url).json()

    if "price" in r:
        return r["price"]
    return None


# /start command
def start(update, context):
    update.message.reply_text(
        "🤖 Trading Bot Ready!\n\n"
        "Commands:\n"
        "/price BTCUSDT\n"
        "/price ETHUSDT\n"
        "/price XRPUSDT"
    )


# /price command
def price(update, context):

    if len(context.args) == 0:
        update.message.reply_text("⚠️ Use: /price BTCUSDT")
        return

    symbol = context.args[0].upper()
    price = get_price(symbol)

    if price:
        msg = f"""
💱 Coin: {symbol}
💰 Price: {price}

🤖 Live Market Data
"""
    else:
        msg = "❌ Invalid Coin Symbol"

    update.message.reply_text(msg)


# 🚀 bot start
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", price))

    print("🤖 Telegram Bot Running...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

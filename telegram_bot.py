from telegram.ext import Updater, CommandHandler
from market import get_price
from config import TOKEN

def start(update, context):
    update.message.reply_text(
        "🤖 Trading Bot सुरू झाला!\n\n"
        "Command:\n"
        "/price BTCUSDT"
    )

def price(update, context):
    if len(context.args) == 0:
        update.message.reply_text("उदाहरण: /price BTCUSDT")
        return

    symbol = context.args[0].upper()
    coin_price = get_price(symbol)

    if coin_price:
        update.message.reply_text(
            f"💰 {symbol}\n"
            f"Price: {coin_price}"
        )
    else:
        update.message.reply_text("❌ Invalid Coin Symbol")

def run_bot():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", price))

    print("🤖 Telegram Bot Started...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()

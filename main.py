import time
from telegram import Bot

from config import TOKEN, CHAT_ID, SYMBOLS, TIMEFRAMES
from market import get_crypto_price
from strategy import ict_smc_signal

bot = Bot(token=TOKEN)

def send(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg)

print("🚀 PRO BOT STARTED")

while True:

    for symbol in SYMBOLS:

        price = get_crypto_price(symbol)
        if not price:
            continue

        for tf in TIMEFRAMES:

            signal, strength = ict_smc_signal(price, tf)

            msg = f"""
🤖 PRO ICT + SMC SIGNAL

💱 Asset: {symbol}
💰 Price: {price}

⏱ Timeframe: {tf}
📊 Signal: {signal}
🎯 Strength: {strength}/100

🌍 Markets: Crypto + Forex + Gold
"""
            send(msg)

            time.sleep(2)

    # cycle delay (3 min system base)
    time.sleep(180)

import time
from telegram import Bot

from config import TOKEN, CHAT_ID, CRYPTO_SYMBOLS, TIMEFRAMES, SCAN_INTERVAL
from market import get_crypto_price
from strategy import ict_smc_signal

bot = Bot(token=TOKEN)


def send_signal(symbol, price, timeframe, signal, strength):

    message = f"""
🚨 TRADING SIGNAL

💱 Coin : {symbol}

💰 Price : {price}

⏰ Timeframe : {timeframe}

📊 Signal : {signal}

🎯 Strength : {strength}%

🤖 Crypto Trading Bot
"""

    bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )


print("🚀 Trading Bot Started...")

while True:

    for symbol in CRYPTO_SYMBOLS:

        try:

            price = get_crypto_price(symbol)

            if price is None:
                continue

            for timeframe in TIMEFRAMES:

                signal, strength = ict_smc_signal(
                    price,
                    timeframe
                )

                if signal != "NO TRADE ⚪":
                    send_signal(
                        symbol,
                        price,
                        timeframe,
                        signal,
                        strength
                    )

                time.sleep(2)

        except Exception as e:
            print(e)

    print("✅ Scan Complete")

    time.sleep(SCAN_INTERVAL)

from telegram import Bot
from config import TOKEN, CHAT_ID

bot = Bot(token=TOKEN)


def send_signal(data):

    message = f"""
🚨 TRADING SIGNAL

💱 Symbol : {data['symbol']}
⏰ Timeframe : {data['timeframe']}

📈 Signal : {data['signal']}

💰 Price : {data['price']}

🤖 Powered By ICT + SMC Bot
"""

    bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )

import random

def ict_smc_signal(price, tf):

    # fake structure engine (upgrade to real candles later)
    strength = random.randint(1, 100)

    if tf == "3m":
        threshold = 65
    elif tf == "15m":
        threshold = 60
    elif tf == "1h":
        threshold = 55
    else:
        threshold = 50

    if strength > threshold:
        signal = "BUY 🟢"
    elif strength < (100 - threshold):
        signal = "SELL 🔴"
    else:
        signal = "NO TRADE ⚪"

    return signal, strength

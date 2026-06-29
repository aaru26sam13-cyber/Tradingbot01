from market import get_klines

def ict_smc_signal(price, timeframe):

    if timeframe == "3m":
        limit = 20
    elif timeframe == "15m":
        limit = 30
    elif timeframe == "1h":
        limit = 40
    else:
        limit = 50

    strength = 60

    if price <= 0:
        return "NO TRADE ⚪", 0

    if timeframe == "3m":
        strength = 75
    elif timeframe == "15m":
        strength = 80
    elif timeframe == "1h":
        strength = 85
    elif timeframe == "4h":
        strength = 90

    signal = "BUY 🟢"

    return signal, strength

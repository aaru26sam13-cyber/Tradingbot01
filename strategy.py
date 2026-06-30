from market import get_klines


def ict_smc_signal(symbol, timeframe):

    candles = get_klines(symbol, timeframe, 50)

    if not candles or len(candles) < 50:
        return "NO TRADE ⚪", 0

    closes = [float(candle[4]) for candle in candles]

    ema20 = sum(closes[-20:]) / 20
    ema50 = sum(closes[-50:]) / 50

    current_price = closes[-1]

    strength = 60

    if ema20 > ema50 and current_price > ema20:
        signal = "BUY 🟢"
        strength = 80

    elif ema20 < ema50 and current_price < ema20:
        signal = "SELL 🔴"
        strength = 80

    else:
        signal = "NO TRADE ⚪"
        strength = 0

    return signal, strength

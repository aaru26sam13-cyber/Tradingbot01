from market import get_klines

def generate_signal(symbol, timeframe="3m"):

    candles = get_klines(symbol, timeframe, 50)

    if not candles or len(candles) < 20:
        return None

    closes = [float(c[4]) for c in candles]

    last = closes[-1]
    avg20 = sum(closes[-20:]) / 20

    if last > avg20:
        signal = "BUY 🟢"
    elif last < avg20:
        signal = "SELL 🔴"
    else:
        signal = "NO TRADE ⚪"

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "price": last,
        "signal": signal,
    }

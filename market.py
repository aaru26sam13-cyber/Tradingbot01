import requests

def get_price(symbol):
    symbol = symbol.upper().strip()   # मोठे अक्षर + space remove

    # 🔥 जर USDT नसेल तर auto add कर
    if "USDT" not in symbol:
        symbol = symbol + "USDT"

    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # ✅ price आला तर ok
        if "price" in data:
            return float(data["price"])

        # ❌ error आला तर print कर
        else:
            print("API Error:", data)
            return None

    except Exception as e:
        print("Error:", e)
        return None

import requests

def get_price(symbol):
    try:
        symbol = symbol.upper().strip()
        symbol = symbol.replace("/PRICE", "").replace("/price", "").strip()

        if "USDT" not in symbol:
            symbol = symbol + "USDT"

        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if "price" in data:
            return float(data["price"])
        else:
            print("DEBUG ERROR:", data)
            return None

    except Exception as e:
        print("ERROR:", e)
        return None

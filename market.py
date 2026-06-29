import requests

BASE_URL = "https://api.binance.com/api/v3"


def get_price(symbol):
    try:
        url = f"{BASE_URL}/ticker/price?symbol={symbol.upper()}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if "price" in data:
            return float(data["price"])

        return None

    except Exception as e:
        print("Price Error:", e)
        return None


def get_klines(symbol, interval="3m", limit=100):
    try:
        url = (
            f"{BASE_URL}/klines?"
            f"symbol={symbol.upper()}&interval={interval}&limit={limit}"
        )

        response = requests.get(url, timeout=10)
        return response.json()

    except Exception as e:
        print("Kline Error:", e)
        return []

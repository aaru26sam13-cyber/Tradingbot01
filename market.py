import requests

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if "price" in data:
            return float(data["price"])
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None

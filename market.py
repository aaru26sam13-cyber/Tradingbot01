import requests

def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    r = requests.get(url).json()
    return float(r["price"]) if "price" in r else None

import requests
def get_crypto_price(coin_id:str, currency: str="usd"):
    url =  f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": currency
    }
    response = requests.get(url, params = params)
    if response.status_code == 200:
        data = response.json()
        if coin_id in data:
            return {
                "coin": coin_id,
                "currency": currency,
                "price": data[coin_id][currency]
            }
        else:
            return {"error":f"Coin '{coin_id}' not found."}
    else:
        return {"error": "Fail to fetch data from CoinGecko"}    

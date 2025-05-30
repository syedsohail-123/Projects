from fastapi import FastAPI
from crypto_service import get_crypto_price
app = FastAPI()
@app.get('/')
def home():
    return {"msg": "Welcome to Crypto Price Tracker API"}
@app.get('/price/{coin}')
def fetch_price(coin: str, currency: str = "usd"):
    return get_crypto_price(coin.lower(), currency.lower())

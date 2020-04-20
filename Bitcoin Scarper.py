import requests

def scarpe():
    response = requests.get(URL+COIN)
    response_json = response.json()
    return float(response_json[0]['price_ind'])


URL = 'https://api.coinmarketcap.com/v1/ticker/'
COIN = "bitcoin"
last_price = None

while True :
    latest_price = scarpe()
    if latest_price != last_price:
        print("Lastest Price:",latest_price)
        last_price = latest_price
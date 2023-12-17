import requests

API_KEY = 'YOUR_API_KEY'
BASE_URL = 'YOUR_URL'

CURRENCIES = ["USD", "EUR", "CAD", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid Currency")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()
    
    if base == "Q":
        break
    
    data = convert_currency(base)
    if not data:
        continue

    data = convert_currency(base)
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

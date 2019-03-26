from django.shortcuts import render
import requests
import json

def home(request):
    # Grab Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD")
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})
    
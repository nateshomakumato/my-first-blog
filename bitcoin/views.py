from django.shortcuts import render
import requests
import json

def index(request):
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XMR,ETH,XRP,LTC&tsyms=INR")
	price = json.loads(price_request.content)

	return render(request, "bitcoin/index.html", {'price' : price})




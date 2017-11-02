import requests
from coinsecure_bot.config.settings import API_KEY,BASE_URL

class CoinSecure():
	def __init__(self):
		pass

	def _getRequest(self,url,extras):
		url = BASE_URL+url
		params = {"accept": "application/json"}.items() + extras.items()
		try:
			response = requests.get(url=url,params=params)
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return 0
		data = response.json()
		return data
		

	def _putRequest(self,url,extras):
		url = BASE_URL+url
		params = {"accept": "application/json"}.items() + extras.items()
		try:
			response = requests.put(url=url,params=params,headers={"Authorization":API_KEY})
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return 0
		data = response.json()
		return data

	def _deleteRequest(self,url,extras):
		url = BASE_URL+url
		params = {"accept": "application/json"}.items() + extras.items()
		try:
			response = requests.delete(url=url,params=params,headers={"Authorization":API_KEY})
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return 0
		data = response.json()
		return data

	def getLowestAskRate(self):
		data = self._getRequest(url="/exchange/ask/low",dict())
		if data['success']:
			return data['message']['rate']
		else:
			return -1
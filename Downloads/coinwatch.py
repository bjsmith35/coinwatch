
import requests
import json
from time import sleep

while True:
  btc = requests.get('https://coinmarketcap-nexuist.rhcloud.com/api/btc')
  eth = requests.get('https://coinmarketcap-nexuist.rhcloud.com/api/eth')
  ltc = requests.get('https://coinmarketcap-nexuist.rhcloud.com/api/ltc')
  xrp = requests.get('https://coinmarketcap-nexuist.rhcloud.com/api/xrp')
  dash = requests.get('https://coinmarketcap-nexuist.rhcloud.com/api/dash')
  xmr = requests.get('https://coinmarketcap-nexuist.rhcloud.com/api/xmr')

  print("")
  print("Bitcoin: ",btc.json()['price']['usd'])
  print("Ethereum: ",eth.json()['price']['usd'])
  print("Litecoin: ",ltc.json()['price']['usd'])
  print("Ripple: ",xrp.json()['price']['usd'])
  print("Dash: ",dash.json()['price']['usd'])
  print("Monero: ",xrp.json()['price']['usd'])
  print("")
  sleep(60)

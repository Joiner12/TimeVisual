#/home/ubuntu/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:42:28 2022

@author: W-H
"""

from binance.client import Client
import os
import matplotlib.pyplot as plt
# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
# set http_proxy=http://127.0.0.1:7890 & set https_proxy=http://127.0.0.1:7890
proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
client = Client(api_key, api_secret, {'proxies': proxies})
print(client.get_server_time())
trades_BTC_USDT = client.get_symbol_ticker(symbol='BTCUSDT')
trades_DOGE_BTC = client.get_symbol_ticker(symbol='DOGEBTC')
trades_DOGE_USDT = float(trades_BTC_USDT['price']) * float(trades_DOGE_BTC['price'])
print(trades_DOGE_USDT)

# import time
# # data procession
# historical_price = list()
# historical_time = list()
# for t in trades:
#     time_temp = t['time'] / 1000
#     time_temp = time.asctime(time.gmtime(time_temp))
#     historical_price.append(t['price'])
#     historical_time.append(time_temp)
#     # historical_price
# plt.plot( historical_price)

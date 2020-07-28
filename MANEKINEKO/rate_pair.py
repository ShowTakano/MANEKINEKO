import requests
import json
import numpy as np
import matplotlib.pyplot as plt

"""
URL = 'https://coincheck.com/api/trades'
params = {"offcet": 0, "pair": "btc_jpy"}
coincheck = requests.get(URL, params=params).json() 
print(coincheck)

URL = 'https://coincheck.com/api/ticker'
coincheck = requests.get(URL, params={"pair": "btc_jpy"}).json()
print(coincheck)
for key, item in coincheck.items():
    print("%-9s : %-10.9s " % (key, item))
"""

def get_rate(num="BTC", den="JPY"):
    ""
    URL = 'https://coincheck.com/api/rate/'
    num = num.lower()
    den = den.lower()
    rate = requests.get(URL + num + "_" + den).json()["rate"]
    rate = float(rate)
    print(num, "/", den, " : ", str(rate))
    return rate

# 取り扱い通貨一覧
coins = [
    "JPY", "BTC", "ETH", "ETC", "LSK", "FCT", "XRP", "XEM", "LTC", "BCH", "MONA", "XLM", "QTUM", "BAT"
]

# 基本レート取得
coin_jpy_rates = []
for i in range(len(coins)):
    rate = get_rate(coins[i], "JPY")
    coin_jpy_rates.append(rate)

# mat作成
# 初期値マップ
mat = np.zeros((len(coins), len(coins)))
for i in range(len(coins)):
    for j in range(len(coins)):
        mat[j][i] = coin_jpy_rates[i] / coin_jpy_rates[j]
        print(coins[i], "/", coins[j], " : ", mat[j][i])

# ヒートマップ表示
plt.figure()
plt.imshow(mat,interpolation='nearest',vmin=0,cmap='jet')
plt.colorbar()
plt.show()

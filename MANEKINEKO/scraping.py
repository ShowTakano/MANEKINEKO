import requests
from bs4 import BeautifulSoup
import re

urlName = "https://coincheck.com/ja/exchange"
#urlName = "https://coincheck.com/ja/buys"
#urlName =  "https://coincheck.com/exchange/tradeview/coincheck/ethjpy"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")

elems = soup.find_all("span")
#elems = soup.find_all(class_="option-rate")

print(elems)

"""
for elem in elems:
    print(elem)
    txt = str(elem)
    if "latest_rates" in txt:
        print("latest_rate is in ----------------------------------")
"""
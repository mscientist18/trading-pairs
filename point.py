import requests

url = 'https://www.binance.com/api/v1/exchangeInfo'
resp = requests.get(url=url)
binanace = resp.json() 

url = 'https://api.coinbase.com/v2/exchange-rates'
resp = requests.get(url=url)
coinbase = resp.json() 

url = 'https://ftx.com/api/markets'
resp = requests.get(url=url)
ftx = resp.json() 

url = 'https://api.kraken.com/0/public/AssetPairs'
resp = requests.get(url=url)
kraken = resp.json() 

url = 'https://api.huobi.pro/v1/common/symbols'
resp = requests.get(url=url)
huobi = resp.json() 


with open('symbols.txt','w') as file:
    file.write("\n\nbinance:\n\n")
    for symbol in binanace['symbols']:
        file.write(symbol['baseAsset']+"/"+symbol["quoteAsset"]+"\n")

    file.write("\n\ncoinbase:\n\n")
    for symbol in coinbase['data']['rates']:
        file.write('USD'+"/"+symbol+"\n")
    
    file.write("\n\nftx:\n\n")
    for symbol in ftx['result']:
        if symbol['baseCurrency']!=None:
            file.write(symbol['baseCurrency']+"/"+symbol['quoteCurrency']+"\n")

    file.write("\n\nkraken:\n\n")
    for key,value in kraken['result'].items():
        file.write(value['base']+"/"+value['quote']+"\n")

    file.write("\n\nhuobi:\n\n")
    for symbol in huobi['data']:
        file.write(symbol['base-currency']+"/"+symbol['quote-currency']+"\n")


            
    






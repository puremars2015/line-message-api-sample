import requests,json

class MyCoinBase:

    def Get(self,currency,currency2):    
        url = "https://api.coinbase.com/v2/exchange-rates?currency=" + currency
        r = requests.get(url)
        obj = json.loads(r.text)
        return obj['data']['rates'][currency2]  

    def GetSupportList(self):
        url = "https://api.coinbase.com/v2/exchange-rates"
        r = requests.get(url)
        obj = json.loads(r.text)
        rs = obj['data']['rates']
        res = []
        for i in rs:
            res.append(i)
        return res

    def Include(self,currency):
        r = self.GetSupportList()
        if (currency in r):
            return True
        else:
            return False

    def SampleAPI(self):
        url = "https://api.coinbase.com/v2/exchange-rates?currency=" + "BTC"
        r = requests.get(url)
        obj = json.loads(r.text)
        return obj['data']['rates']['TWD']  

    def Sample(self):
        r = self.GetSupportList()
        print(r)


# cb = MyCoinBase()
# r = cb.Get(currency='BTC',currency2='TWD')
# print(r)

cb = MyCoinBase()
r = cb.SampleAPI()
print(r)
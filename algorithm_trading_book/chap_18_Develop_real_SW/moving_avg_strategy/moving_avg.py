# import pandas as pd
import pandas_datareader.data as web
from pandas import to_numeric
# import matplotlib.pyplot as plt

jongmok_code = ["069410", "299900","007690","145990","005380","361610","101170","373220","294630","003670"]
jongmok_name = ["Ntells", "Wisiwig","Gukdo","Samyang","HMC","SKIETech","Woorim","LGenergy","Seonam","POSCOchemical"]
criteria_list={}
# index=0
for code in jongmok_code:
    gs = web.DataReader(code, "naver", "2022-05-01")
    gs = gs.apply(to_numeric) #naver는 데이터가 string이여서 numeric로 변경 필요. yahoo는 필요없음

    ma5=gs['Close'].rolling(window=5).mean()  #yahoo는 'Adj Close', naver는 'Close'
    ma20=gs['Close'].rolling(window=20).mean()
    ma60=gs['Close'].rolling(window=60).mean()
    ma120=gs['Close'].rolling(window=120).mean()
    sell_on=(ma5[-2]>=ma20[-2]) and (ma5[-1]<ma20[-1])
    buy_on=(ma5[-2]<=ma20[-2]) and (ma5[-1]>ma20[-1])
    criteria_list[code]=[sell_on,buy_on]

print(criteria_list)
# print(criteria_list[jongmok_code[0]][0])
# print(gs['Volume']!=0), 공휴일(거래량=0) 데이터가 원본에 없어서 코드는 무의미 함

    # gs.insert(len(gs.columns), "MA5", ma5)
    # gs.insert(len(gs.columns), "MA20", ma20)
    # gs.insert(len(gs.columns), "MA60", ma60)
    # gs.insert(len(gs.columns), "MA120", ma120)

# print(gs.tail(20))
# print(gs['MA5'][-2])



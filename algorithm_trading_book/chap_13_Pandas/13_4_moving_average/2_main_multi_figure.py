import pandas as pd
import pandas_datareader.data as web
from pandas import to_numeric
import matplotlib.pyplot as plt

jongmok_code = ["069410", "299900","007690","145990","005380","361610","101170","373220","294630","005930","068270","010120","024880","001440","352820"]
jongmok_name = ["Ntells", "Wisiwig","Gukdo","Samyang","HMC","SKIETech","Woorim","LGenergy","Seonam","SEC","Seltrion","LSElec","KPF","DAEHAN_Wire","HIVE"]
index=0
for code in jongmok_code:
    gs = web.DataReader(code, "naver", "2022-05-01")
    gs = gs.apply(to_numeric) #naver는 데이터가 string이여서 numeric로 변경 필요. yahoo는 필요없음
# print(gs.tail())
    ma5=gs['Close'].rolling(window=5).mean()  #yahoo는 'Adj Close', naver는 'Close'
    ma20=gs['Close'].rolling(window=20).mean()
    ma60=gs['Close'].rolling(window=60).mean()
    ma120=gs['Close'].rolling(window=120).mean()
# print(ma5.tail(10))
# print(gs['Volume']!=0), 공휴일(거래량=0) 데이터가 원본에 없어서 코드는 무의미 함
    gs.insert(len(gs.columns), "MA5", ma5)
    gs.insert(len(gs.columns), "MA20", ma20)
    gs.insert(len(gs.columns), "MA60", ma60)
    gs.insert(len(gs.columns), "MA120", ma120)
    # print(gs.tail(20))
    # plt.figure(index)
    plt.figure(index, figsize=(10,6))
    plt.title(jongmok_name[index])
    plt.plot(gs.index, gs['Close'], label="Close")
    plt.plot(gs.index, gs['MA5'], label='MA5')
    plt.plot(gs.index, gs['MA20'], label='MA20')
    plt.plot(gs.index, gs['MA60'], label='MA60')
    plt.plot(gs.index, gs['MA120'], label='MA120')

    plt.legend(loc="best")
    plt.grid()
    index=index+1
plt.show()


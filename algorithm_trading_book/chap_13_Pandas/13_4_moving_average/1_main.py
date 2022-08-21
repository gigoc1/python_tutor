import pandas as pd
import pandas_datareader.data as web
gs = web.DataReader("TSLA", "yahoo", "2022-01-01")
# print(gs.tail())
ma5=gs['Adj Close'].rolling(window=5).mean()
ma20=gs['Adj Close'].rolling(window=20).mean()
ma60=gs['Adj Close'].rolling(window=60).mean()
ma120=gs['Adj Close'].rolling(window=120).mean()
# print(ma5.tail(10))
# print(gs['Volume']!=0), 공휴일(거래량=0) 데이터가 원본에 없어서 코드는 무의미 함
gs.insert(len(gs.columns), "MA5", ma5)
gs.insert(len(gs.columns), "MA20", ma20)
gs.insert(len(gs.columns), "MA60", ma60)
gs.insert(len(gs.columns), "MA120", ma120)
print(gs.tail(20))

import matplotlib.pyplot as plt
plt.plot(gs.index, gs['Adj Close'], label="Adj Close")
plt.plot(gs.index, gs['MA5'], label='MA5')
plt.plot(gs.index, gs['MA20'], label='MA20')
plt.plot(gs.index, gs['MA60'], label='MA60')
plt.plot(gs.index, gs['MA120'], label='MA120')

plt.legend(loc="best")
plt.grid()
plt.show()
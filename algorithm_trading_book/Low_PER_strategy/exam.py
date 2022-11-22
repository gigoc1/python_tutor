from pykrx import stock
import pandas as pd
import time
import numpy as np

df1 = stock.get_market_cap("20210101", alternative=True)
print(df1)
df1 = df1[["종가", "시가총액"]]
print(df1)
df1.columns = ["시가", "시가총액"]
print(df1)
df1 = df1.sort_values('시가총액')
df1['group'] = pd.cut(df1.reset_index().index, bins=3, labels=['소형주', '중형주', '대형주'])
print(df1)
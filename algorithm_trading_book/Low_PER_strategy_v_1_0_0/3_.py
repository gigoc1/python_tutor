from pykrx import stock
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt


def low_per_pbr(year):
    df1 = stock.get_market_cap(f"{year}0101", alternative=True, market='ALL')
    df1 = df1[["종가", "시가총액"]]
    df1.columns = ["시가", "시가총액"]
    # df1 = df1.sort_values('시가총액')
    # df1['group'] = pd.cut(df1.reset_index().index, bins=3, labels=['소형주', '중형주', '대형주'])

    df2 = stock.get_market_fundamental(f"{year}0101", alternative=True, market='ALL')
    df2 = df2[['PER', 'PBR']]
    # df2 = df2.query('PER != 0').copy()
    df2 = df2.sort_values('PER') #수정
    df2['group'] = pd.cut(df2.reset_index().index, bins=3, labels=['저PER', '중PER', '고PER'])

    df3 = stock.get_market_ohlcv(f"{year}1231", alternative=True, market='ALL')
    df3 = df3[['종가']]

    t0 = pd.merge(left=df1, right=df2, left_index=True, right_index=True)
    df = pd.merge(left=df3, right=t0, left_index=True, right_index=True)

    df = df.query('PBR != 0').copy()
    df['수익률'] = df['종가'] / df['시가']
    # cond = (df['PER'] >= 2.5) & (df['PER'] <= 10)
    # top30 = df[cond].sort_values('PBR').groupby('group').head(30)
    top30 = df.sort_values('PBR').groupby('group').head(30)

    how = {
        '수익률' : np.mean
    }
    yoy = top30.groupby('group').agg(how)
    yoy.columns = [year]
    return yoy

dfs = [ ]
for date in range(2010, 2022):
    df = low_per_pbr(f"{date}")
    dfs.append(df)
    time.sleep(1)

df = pd.concat(dfs, axis=1)
print(df.cumprod(axis=1))
df.cumprod(axis=1).transpose().plot.line()
plt.show()
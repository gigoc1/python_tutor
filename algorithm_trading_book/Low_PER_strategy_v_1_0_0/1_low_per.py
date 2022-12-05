import pandas as pd
import numpy as np

df_factor = pd.read_excel(
    "data/data_2900_20221120.xlsx", 
    index_col=0, 
    usecols=[0, 1, 6, 10]   # 종목코드, 종목명, PER, PBR
)
# print(df_factor.info())
df_factor.replace('-', np.nan, inplace=True)
# print(df_factor.head())

df_volume = pd.read_excel("data/data_2954_20221120.xlsx", index_col=0, usecols=[0, 9])
# print(df_volume.head())

df2 = df_factor.join(df_volume)
# print(df2.head())

df_change = pd.read_excel("data/data_3105_20221120.xlsx", index_col=0, usecols=[0, 5])
# print(df_change.head())

df3 = df2.join(df_change)
# print(df3.head())

cond = df3['거래량'] != 0
df4 = df3[cond].copy()

df5 = df4.sort_values(by="PER", ascending=True)
df5.reset_index(inplace=True)
# print(df5)

low_per30 = df5.iloc[:30]
# print(low_per30['등락률'].mean())

df5['group'] = pd.cut(df5.index, bins=20, labels=False)    # group 컬럼 추가
df6 = df5.groupby(by='group')[['등락률']].mean()
print(df6)

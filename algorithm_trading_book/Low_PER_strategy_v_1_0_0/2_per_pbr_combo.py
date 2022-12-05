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

cond = (df4['PER'] >= 2.5) & (df4['PER'] <= 10)
df5 = df4[cond].copy()
# print(df5)

df6 = df5.sort_values(by='PBR')[:30]
print(df6.describe())
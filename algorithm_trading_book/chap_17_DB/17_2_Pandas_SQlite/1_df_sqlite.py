import pandas as pd
from pandas import Series, DataFrame
import sqlite3
raw_data = {'col0': [1, 2, 3, 4], 'col1': [10, 20, 30, 60], 'col2':[100, 200, 300, 400]}
df = DataFrame(raw_data)
print(df)

con=sqlite3.connect("C:\\Users\\Administrator\\Documents\\kospi.db")

df.to_sql('test', con, if_exists='replace') # db에 테이블이 기존재하면 error 발생-->if_exists='replace'

df1=pd.read_sql("SELECT * FROM test", con, index_col='index') 

print(df1)
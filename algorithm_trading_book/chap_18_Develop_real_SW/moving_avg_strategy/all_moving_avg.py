import pandas as pd
import pandas_datareader.data as web
from pandas import to_numeric

url = 'https://kind.krx.co.kr/corpgeneral/corpList.do'
jongmok_code_kp = pd.read_html(url+"?method=download&marketType=stockMkt")[0]
jongmok_code_kp = jongmok_code_kp['종목코드']

jongmok_code_kq = pd.read_html(url+"?method=download&marketType=kosdaqMkt")[0]
jongmok_code_kq = jongmok_code_kq['종목코드']

jongmok_code = pd.concat([jongmok_code_kp,jongmok_code_kq], ignore_index=True)

def make_code_ks(x):
    x = str(x)
    return '0'*(6-len(x))+x

jongmok_code = jongmok_code.apply(make_code_ks)

criteria_list={}

def moving_avg():
    for code in jongmok_code:
        gs = web.DataReader(code, "naver", "2022-05-01")
        gs = gs.apply(to_numeric) #naver는 데이터가 string이여서 numeric로 변경 필요. yahoo는 필요없음

        ma5=gs['Close'].rolling(window=5).mean()  #yahoo는 'Adj Close', naver는 'Close'
        ma20=gs['Close'].rolling(window=20).mean()
        # ma60=gs['Close'].rolling(window=60).mean()
        # ma120=gs['Close'].rolling(window=120).mean()
        sell_on=(ma5[-2]>=ma20[-2]) and (ma5[-1]<ma20[-1])
        buy_on=(ma5[-2]<=ma20[-2]) and (ma5[-1]>ma20[-1])
        if sell_on or buy_on:
            criteria_list[code]=[sell_on,buy_on, gs['Close'][-1]]
    return criteria_list
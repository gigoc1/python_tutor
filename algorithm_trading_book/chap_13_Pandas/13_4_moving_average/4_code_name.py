import sys
import pandas as pd
import pandas_datareader.data as web
from pandas import to_numeric

input_name=sys.argv[1]

url = 'https://kind.krx.co.kr/corpgeneral/corpList.do'
jongmok_code_kp = pd.read_html(url+"?method=download&marketType=stockMkt")[0]
jongmok_code_kp = jongmok_code_kp[['종목코드','회사명']]

jongmok_code_kq = pd.read_html(url+"?method=download&marketType=kosdaqMkt")[0]
jongmok_code_kq = jongmok_code_kq[['종목코드','회사명']]

jongmok_code = pd.concat([jongmok_code_kp,jongmok_code_kq], ignore_index=True)

def make_code_ks(x):
    x = str(x)
    return '0'*(6-len(x))+x

jongmok_code['종목코드'] = jongmok_code['종목코드'].apply(make_code_ks)
# input_df = jongmok_code.loc[input_name in jongmok_code['회사명']]  #특정 컬럼과 일치하는 DF 추출

input_jongmok=[[]]
if input_name.isdigit():  # 실행 인자로 종목코드 입력 시
    input_df = jongmok_code.loc[jongmok_code['종목코드']==input_name]
    input_jongmok=input_df.values.tolist()[0]
else:
    input_df = jongmok_code.loc[jongmok_code['회사명'].str.contains(input_name)]  #특정 문자열을 포함하는 DF 추출(df['name'].str.contains('format'))
    input_jongmok=input_df.values.tolist()[0]  # DF에서 리스트 추출 (예: ['002345','현대자동차'])

gs = web.DataReader(str(input_jongmok[0]), "naver", "2022-01-01")
gs = gs.apply(to_numeric) #naver는 데이터가 string이여서 numeric로 변경 필요. yahoo는 필요없음

ma5=gs['Close'].rolling(window=5).mean()  #yahoo는 'Adj Close', naver는 'Close'
ma20=gs['Close'].rolling(window=20).mean()
# trade_amount=gs['Volume']
# ma60=gs['Close'].rolling(window=60).mean()
# ma120=gs['Close'].rolling(window=120).mean()

gs.insert(len(gs.columns), "MA5", ma5)
gs.insert(len(gs.columns), "MA20", ma20)
# gs.insert(len(gs.columns), "MA60", ma60)
# gs.insert(len(gs.columns), "MA120", ma120)
print(gs.tail(20))

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

import matplotlib.pyplot as plt
fig, ax1=plt.subplots() # subplot 관련 자료 검색 필요
fig.suptitle(input_jongmok[1]) 
line1=ax1.plot(gs.index, gs['Close'], marker='o', markersize=3, label="Close")
line2=ax1.plot(gs.index, gs['MA5'], marker='o', markersize=3, label='MA5')
line3=ax1.plot(gs.index, gs['MA20'], marker='o', markersize=3, label="MA20")
# plt.plot(gs.index, gs['MA60'], label='MA60')
# plt.plot(gs.index, gs['MA120'], label='MA120')

ax2=ax1.twinx()
line4=ax2.plot(gs.index, gs['Volume'], color = 'black', marker='o', markersize=3, label="Volume")

lines = line1+line2+line3 +line4
labels = [l.get_label() for l in lines]

ax1.legend(lines, labels, loc="best")
plt.grid()
plt.show()

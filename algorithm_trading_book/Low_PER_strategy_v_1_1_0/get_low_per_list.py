from pykrx import stock
import pandas as pd

def get_low_per_pbr(date):
    df1 = stock.get_market_cap(f"{date}", alternative=True, market="ALL")
    df1 = df1[["종가", "시가총액"]]
    df1.columns = ["시가", "시가총액"]
    # df1 = df1.sort_values('시가총액')
    # df1['group'] = pd.cut(df1.reset_index().index, bins=3, labels=['소형주', '중형주', '대형주'])

    df2 = stock.get_market_fundamental(f"{date}", alternative=True, market="ALL")
    df2 = df2[['PER', 'PBR']]
    # df2 = df2.query('PER != 0').copy()
    df2 = df2.sort_values('PER') #수정
    df2['group'] = pd.cut(df2.reset_index().index, bins=3, labels=['저PER', '중PER', '고PER'])

    df3 = stock.get_market_ohlcv(f"{date}", alternative=True, market="ALL")
    # stock_code = stock.get_market_ticker_list(date, market="ALL")
    stock_code = [item for item in df3.index]
    stock_name=[]
    for code in stock_code:
        name=stock.get_market_ticker_name(code)
        stock_name.append(name)
    df_stock_name = pd.DataFrame.from_records(stock_name)
    df3['종목명']=stock_name

    t0 = pd.merge(left=df1, right=df2, left_index=True, right_index=True)
    df = pd.merge(left=df3, right=t0, left_index=True, right_index=True)

    df = df.query('PBR != 0 and 거래량 != 0').copy()
    # df['수익률'] = df['종가'] / df['시가']
    # cond = (df['PER'] >= 2.5) & (df['PER'] <= 10)
    # top30 = df[cond].sort_values('PBR').groupby('group').head(30)
    top_list = df.sort_values('PBR').groupby('group').head(50)
    top_list.to_excel('Low_PER.xlsx')
    cond1=top_list['group']=="저PER"
    top_list=top_list[cond1]
    print(top_list)
    top=[item for item in top_list.index]

    return top

get_low_per_pbr(20221201)
import re
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

def get_financial_statements(code):
    re_enc = re.compile("encparam: '(.*)'", re.IGNORECASE)
    re_id = re.compile("id: '([a-zA-Z0-9]*)' ?", re.IGNORECASE)

    url = "http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd={}".format(code)
    html = requests.get(url).text
    encparam = re_enc.search(html).group(1)
    encid = re_id.search(html).group(1)

    url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd={}&fin_typ=0&freq_typ=A&encparam={}&id={}".format(code, encparam, encid)
    headers = {"Referer": "HACK"}
    html = requests.get(url, headers=headers).text

    dfs = pd.read_html(html)
    df = dfs[1]['연간연간컨센서스보기']
    df.index = dfs[1]['주요재무정보'].values.flatten()
    df = df.loc['현금배당수익률']
    df.index = df.index.str[:7]

    return df.to_dict()

def get_dividend_yield(code):
    url = "http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html5lib') 
    dt_data = soup.select("td dl dt")

    dividend_yield = dt_data[-2].text 
    dividend_yield = dividend_yield.split(' ')[1] 
    dividend_yield = dividend_yield[:-1]

    return dividend_yield

def get_estimated_dividend_yield(code):
    dividend_yield = get_financial_statements(code) 
    dividend_yield = sorted(dividend_yield.items())[-1] 
    return dividend_yield[1]

def get_3year_treasury():
    url = "http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=288401&amp;idx_cd=2884&amp;freq=Y&amp;period=1998:2016"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    td_data = soup.select("tr td")
    print(html)

def get_current_3year_treasury():
    url = "http://finance.naver.com/marketindex/interestDailyQuote.nhn?marketindexCd=IRR_GOVT03Y&page=1"
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html5lib') 
    td_data = soup.select("tr td") 
    return td_data[1].text

def get_previous_dividend_yield(code):
    dividend_yield = get_financial_statements(code)  

    now = datetime.datetime.now()
    cur_year = now.year

    previous_dividend_yield = {}

    for year in range(cur_year-5, cur_year):
        if str(str(year)+"/12") in dividend_yield.keys():
            previous_dividend_yield[str(str(year)+"/12")] = dividend_yield[str(str(year)+"/12")]

    return previous_dividend_yield

if __name__ == "__main__":
    dividend_yield = get_dividend_yield('058470')
    print(dividend_yield)
    estimated_dividend_yield = get_estimated_dividend_yield('058470') 
    print(estimated_dividend_yield)
    print(get_current_3year_treasury())
    print(get_previous_dividend_yield('058470'))
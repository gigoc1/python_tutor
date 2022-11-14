from bs4 import BeautifulSoup
from pykrx import stock
import requests
import pandas as pd

def get_corp_code():
    url = "http://comp.fnguide.com/XML/Market/CompanyList.txt"
    resp = requests.get(url)
    resp.encoding = "utf-8-sig"
    data = resp.json()
    comp = data['Co']
    df = pd.DataFrame(data=comp)
    cond = df['gb'] == '701'
    df2 = df[cond].copy()
    return df2

def get_closing_accounts_day(code):
    url = f"https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{code}"
    selector = "#compBody > div.section > div.corp_group1 > p > span.stxt"
    resp = requests.get(url)
    html = resp.text 

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select(selector)
    return tags[1].text

df = get_corp_code()
s = df.iloc[0]
acode = s['cd']
code = acode[1:]
print(code)
print(get_closing_accounts_day(code))

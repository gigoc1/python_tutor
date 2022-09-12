import requests
from bs4 import BeautifulSoup

def get_3year_treasury():
    url = "https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1073"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    td_data = soup.select("tr:nth-of-type(1) td")
    print(td_data[16].text)

if __name__ == "__main__":
    get_3year_treasury()
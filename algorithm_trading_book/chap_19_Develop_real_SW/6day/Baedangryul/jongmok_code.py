import pandas as pd

def code_list():
    url = 'https://kind.krx.co.kr/corpgeneral/corpList.do'
    jongmok_code_kp = pd.read_html(url+"?method=download&marketType=stockMkt")[0]
    jongmok_code_kp = jongmok_code_kp['종목코드']

    jongmok_code_kq = pd.read_html(url+"?method=download&marketType=kosdaqMkt")[0]
    jongmok_code_kq = jongmok_code_kq['종목코드']

    jongmok_code = pd.concat([jongmok_code_kp,jongmok_code_kq], ignore_index=True)
    jongmok_code = jongmok_code.apply(make_code_ks)

    return jongmok_code

def make_code_ks(x):
    x = str(x)
    return '0'*(6-len(x))+x
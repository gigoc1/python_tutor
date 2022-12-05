import pandas as pd
import numpy as np

def get_ev_ebitda(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A{code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701"
    try:
        dfs = pd.read_html(url)
        df = dfs[3]
        # print(df)
        df.set_index(df.columns[0], inplace=True)
        ev_ebitda = df.filter(like="EV/EBITDA", axis=0).filter(regex="^2021").iloc[0, 0]
        ev_ebitda = float(ev_ebitda)
    except:
        ev_ebitda = np.nan
    return ev_ebitda
print(get_ev_ebitda('138930'))
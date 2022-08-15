import win32com.client #크레온관련
import sys
import time
import datetime
from numpy import true_divide
import pyautogui
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

#자동입력
'''
def macro_text(img,x,y,confidence,val):
    img_text_input = pyautogui.locateOnScreen(img, confidence)      
    if img_text_input!=None:            
        pyautogui.click(x=img_text_input.left+x,y=img_text_input.top+y)                
        pyautogui.typewrite(val, interval=0.2)
        time.sleep(0.3)    

#자동클릭
def macro_click(img,x,y,confidence):
    img_text_input = pyautogui.locateOnScreen(img, confidence)  
    if img_text_input!=None:            
        pyautogui.click(x=img_text_input.left+x,y=img_text_input.top+y)                
        time.sleep(0.5)
'''

#매수하는 함수
def stock_buy(acc,code,price,count):
    #https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=174&page=3&searchString=%eb%a7%a4%ec%88%98&p=8841&v=8643&m=9505 매수참고
    accFlag = objTrade.GoodsList(acc, 1)  # 주식상품 구분 
    objStockOrder = win32com.client.Dispatch("CpTrade.CpTd0311")
    objStockOrder.SetInputValue(0, "2")   # 2: 매수
    objStockOrder.SetInputValue(1, acc )   #  계좌번호
    objStockOrder.SetInputValue(2, accFlag[0])   # 상품구분 - 주식 상품 중 첫번째
    objStockOrder.SetInputValue(3, "A"+str(code))   # 종목코드 - A003540 - 대신증권 종목
    objStockOrder.SetInputValue(4, count)   # 매수수량 10주
    objStockOrder.SetInputValue(5, price)   # 주문단가  - 14,100원
    objStockOrder.SetInputValue(7, "0")   # 주문 조건 구분 코드, 0: 기본 1: IOC 2:FOK
    objStockOrder.SetInputValue(8, "01")   # 주문호가 구분코드 - 01: 보통
    objStockOrder.BlockRequest()
    rqStatus = objStockOrder.GetDibStatus()
    rqRet = objStockOrder.GetDibMsg1()
    #print("통신상태", rqStatus, rqRet)
    #if rqStatus == 0:
    #    print("거래성공"+str(rqStatus))
    #else:
    #    print("1거래실패"+str(rqStatus))
    return str(rqStatus)

#매도하는 함수
def stock_sale(acc,code,price,count):
    #https://money2.creontrade.com/e5/mboard/ptype_basic/plusPDS/DW_Basic_Read.aspx?boardseq=299&seq=47&page=2&searchString=%eb%a7%a4%eb%8f%84&prd=&lang=7&p=8833&v=8639&m=9505 매도참고
    accFlag = objTrade.GoodsList(acc, 1)  # 주식상품 구분
    objStockOrder = win32com.client.Dispatch("CpTrade.CpTd0311")
    objStockOrder.SetInputValue(0, "1")   #  1: 매도
    objStockOrder.SetInputValue(1, acc )   #  계좌번호
    objStockOrder.SetInputValue(2, accFlag[0])   #  상품구분 - 주식 상품 중 첫번째
    objStockOrder.SetInputValue(3, "A"+str(code))   #  종목코드 - A003540 - 대신증권 종목
    objStockOrder.SetInputValue(4, count)   #  매도수량 10주
    objStockOrder.SetInputValue(5, price)   #  주문단가  - 14,100원
    objStockOrder.SetInputValue(7, "0")   #  주문 조건 구분 코드, 0: 기본 1: IOC 2:FOK
    objStockOrder.SetInputValue(8, "01")   # 주문호가 구분코드 - 01: 보통
    # 매도 주문 요청
    objStockOrder.BlockRequest()   
    rqStatus = objStockOrder.GetDibStatus()
    rqRet = objStockOrder.GetDibMsg1()    
    #if rqStatus == 0:
    #    print("거래성공"+str(rqStatus))
    #else:
    #    print("2거래실패"+str(rqStatus))
    return str(rqStatus)


time.sleep(3)
 
# 연결 여부 체크
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS가 정상적으로 연결되지 않음. ")
    exit()
 
# 주문 초기화
objTrade =  win32com.client.Dispatch("CpTrade.CpTdUtil")
initCheck = objTrade.TradeInit(0)
if (initCheck != 0):
    print("주문 초기화 실패")
    exit()
 
 
# 주식 매수 주문
my_acc = objTrade.AccountNumber[0] #계좌번호    


val1=sys.argv[1] #아이디
#val2=sys.argv[2] #비밀번호
time_start="09:00:00"#시작시간
time_end="15:25:00"#종료시간

tm_wday=(time.localtime().tm_wday)#요일
tm_hour=(time.localtime().tm_hour)#시간
dt_now = datetime.datetime.now()

s_s_code=""
s_price=""
s_s_count=""
b_s_code=""
b_price=""
b_s_count=""
return_buy="" #구매리턴값
return_sale="" #판매리턴값



while True:
    return_buy="" #초기화    
    return_sale="" #초기화
    return_data=""
        
    dt_now = datetime.datetime.now()

    #월~금 8~16시까지
    #if tm_wday!=5 and tm_wday!=6 and tm_hour>=8  and tm_hour<16 : 
    #if True:
    #if tm_wday!=5 and tm_wday!=6 and time_start <= str(dt_now.strftime('%H:%M:%S')) and str(dt_now.strftime('%H:%M:%S')) <= time_end :    
    if time_start <= str(dt_now.strftime('%H:%M:%S')) and str(dt_now.strftime('%H:%M:%S')) <= time_end :    
        #xml정보호출            
        webpage = requests.get("http://finance.ssbang.net/autostock.php?user_id="+val1)
        #webpage = requests.get("http://finance.ssbang.net/autostock_temp.php")
        soup = BeautifulSoup(webpage.content, "html.parser")                      
                

        #매도하기
        s_price=""#초기화
        s_s_code=""
        s_s_count=""
        if soup.findAll("stock")[0].s_run.string=="true":#값을실행해야하는경우
            s_price=soup.findAll("stock")[0].s_price.string#금액입력
            s_s_code=soup.findAll("stock")[0].s_code.string#종목코드
            s_s_count=soup.findAll("stock")[0].s_count.string#수량
            #매도하는 함수 (종목코드,매도금액,매도갯수)            
            return_sale=stock_sale(acc=my_acc,code=s_s_code,price=s_price,count=s_s_count)
            


        #매수하기
        b_price=""#초기화
        b_s_code=""
        b_s_count=""
        if soup.findAll("stock")[1].s_run.string=="true":#값을실행해야하는경우
            b_price=soup.findAll("stock")[1].s_price.string#금액입력
            b_s_code=soup.findAll("stock")[1].s_code.string#종목코드
            b_s_count=soup.findAll("stock")[1].s_count.string#수량            
            #매수하는 함수 (종목코드,매수금액,매수갯수)            
            return_buy=stock_buy(acc=my_acc,code=b_s_code,price=b_price,count=b_s_count)           
            
                

        if soup.findAll("stock")[0].s_run.string=="true" or soup.findAll("stock")[1].s_run.string=="true" :#내용이 있으면 실행            
            #매매내역을 업데이트 처리해주는 부분
            return_data="sale:"
            return_data+=s_s_code+":"
            return_data+=s_price+":"
            return_data+=s_s_count+":"
            return_data+=";buy:"
            return_data+=b_s_code+":"
            return_data+=b_price +":"
            return_data+=b_s_count +":"            
            #처리결과를 전송해줌
            if return_sale=="0" or return_buy=="0" :                
                urlopen("http://finance.ssbang.net/autostock_update.php?user_id="+val1+"&return_data="+return_data) #필드초기화및 프로그램 가동여부 기록
                print("[현재시간:"+str(dt_now.strftime('%H:%M:%S'))+"] "+return_data)                
            else :
                print("[현재시간:"+str(dt_now.strftime('%H:%M:%S'))+"] 정상처리되지 않았습니다 return_sale:"+return_sale+", return_buy:"+return_buy)                
            
            time.sleep(10)#딜레이
        else :#내용이 없으면 1분딜레이
            print("[현재시간:"+str(dt_now.strftime('%H:%M:%S'))+"] 매매한 내역이 없음")            
            time.sleep(60)#딜레이  
        
    else:
        print("[현재시간:"+str(dt_now.strftime('%H:%M:%S'))+"] 지금은 장 시간이 아닙니다")        
        time.sleep(60)#딜레이

    #프로그램 종료
    if str(dt_now.strftime('%H:%M'))=="15:35":#프로그램종료
        sys.exit()#종료하기

            

    #요일시간내에작동 end
#while end
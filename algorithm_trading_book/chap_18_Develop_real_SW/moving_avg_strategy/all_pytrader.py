from posixpath import split
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from Kiwoom import *
from all_moving_avg import moving_avg

form_class = uic.loadUiType("pytrader.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()

        self.trade_stocks_done = False

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.timer2 = QTimer(self)
        self.timer2.start(1000*60*10)
        self.timer2.timeout.connect(self.timeout2)

        self.timer3 = QTimer(self)
        self.timer3.start(1000*60*30)
        self.timer3.timeout.connect(self.timeout3)

        accouns_num = int(self.kiwoom.get_login_info("ACCOUNT_CNT"))
        accounts = self.kiwoom.get_login_info("ACCNO")

        accounts_list = accounts.split(';')[0:accouns_num]
        self.comboBox.addItems(accounts_list)

        self.lineEdit.textChanged.connect(self.code_changed)
        self.pushButton.clicked.connect(self.send_order)
        self.pushButton_2.clicked.connect(self.check_balance)

        self.load_buy_sell_list()

    def timeout(self):
        # market_start_time = QTime(9, 0, 0)
        current_time = QTime.currentTime()

        # if current_time > market_start_time and self.trade_stocks_done is False:
        #     self.trade_stocks()
        #     self.trade_stocks_done = True

        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간: " + text_time

        state = self.kiwoom.GetConnectState()
        if state == 1:
            state_msg = "서버 연결 중"
        else:
            state_msg = "서버 미 연결 중"

        self.statusbar.showMessage(state_msg + " | " + time_msg)

    def timeout2(self):
        print("timeout2: "+QTime.currentTime().toString("hh:mm:ss"))
        if self.checkBox.isChecked():
            self.check_balance()

                # 일정 수익율 이상 종목 매도
        account = self.comboBox.currentText()
        stock_row_count=self.tableWidget_2.rowCount()
        if stock_row_count > 0: #조회 종목 없을때 에러 방지, 테이블 기본 행 갯수는 0으로 셋팅(QtDesigner)
            for index in range(0,stock_row_count):
                code=str(self.tableWidget_2.item(index,1).text()).replace('A','')
                num=self.tableWidget_2.item(index,2).text()
                price=0
                if float(self.tableWidget_2.item(index,6).text()) >= 20.0:
                    self.kiwoom.send_order("send_order_req", "0101", account, 2, code, num, price, "03", "")  #매도
                    print("trade sell over earning rate")
                    time.sleep(0.2)

    def timeout3(self):
        print("timeout3: "+QTime.currentTime().toString("hh:mm:ss"))
        stock_keep={} #{종목명:수량}
        stock_row_count=self.tableWidget_2.rowCount()
        if stock_row_count > 0: #조회 종목 없을때 에러 방지, 테이블 기본 행 갯수는 0으로 셋팅(QtDesigner)
            for index in range(0,stock_row_count):
                stock_keep[self.tableWidget_2.item(index,0).text()]=self.tableWidget_2.item(index,2).text()
        
        criteria_list=moving_avg()
        
        f = open("buy_list_2.txt", 'wt', encoding='UTF-8')
        for code in criteria_list:
            name = self.kiwoom.get_master_code_name(code)
            number=0 if (stock_keep.get(name)==None) else stock_keep.get(name)
            f.writelines(name+";"+code+";시장가;"+str(number)+";"+str(criteria_list[code][2])+";"+str(criteria_list[code][0])
                        +";"+str(criteria_list[code][1])+"\n")
        f.close()

        self.trade_stocks()
        self.load_buy_sell_list()

    def code_changed(self):
        code = self.lineEdit.text()
        name = self.kiwoom.get_master_code_name(code)
        self.lineEdit_2.setText(name)

    def send_order(self):
        order_type_lookup = {'신규매수': 1, '신규매도': 2, '매수취소': 3, '매도취소': 4}
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        account = self.comboBox.currentText()
        order_type = self.comboBox_2.currentText()
        code = self.lineEdit.text()
        hoga = self.comboBox_3.currentText()
        num = self.spinBox.value()
        price = self.spinBox_2.value()

        self.kiwoom.send_order("send_order_req", "0101", account, order_type_lookup[order_type], code, num, price, hoga_lookup[hoga], "")

    def check_balance(self):
        self.kiwoom.reset_opw00018_output()
        account_number = self.kiwoom.get_login_info("ACCNO")
        account_number = account_number.split(';')[0]

        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")

        while self.kiwoom.remained_data:
            time.sleep(0.2)
            self.kiwoom.set_input_value("계좌번호", account_number)
            self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 2, "2000")

        # opw00001
        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00001_req", "opw00001", 0, "2000")

        # balance
        item = QTableWidgetItem(self.kiwoom.d2_deposit)
        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tableWidget.setItem(0, 0, item)

        for i in range(1, 6):
            try:   # "IndexError: list index out of range" 발생하여 처리
                item = QTableWidgetItem(self.kiwoom.opw00018_output['single'][i - 1])
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.tableWidget.setItem(0, i, item)
            except IndexError as e:
                print("IndexError")
        self.tableWidget.resizeRowsToContents()

        # Item list
        self.tableWidget_2.setSortingEnabled(False)
        item_count = len(self.kiwoom.opw00018_output['multi'])
        self.tableWidget_2.setRowCount(item_count)

        for j in range(item_count):
            row = self.kiwoom.opw00018_output['multi'][j]
            for i in range(len(row)):
                item = QTableWidgetItem(row[i])
                item_refresh=QTableWidgetItem()    #QTableWidgetItem에 숫자로 입력할 때는 item_refresh처럼 빈 객체 만들고, setData 함수 이용 필요
                if i<2:   # 테이블 데이터 정렬을 위해 숫자와 문자열 구분하여 입력
                    self.tableWidget_2.setItem(j, i, item)
                elif i >= 2 and i<6:
                    item_refresh.setData(Qt.DisplayRole, int(str(row[i]).replace(',','')))  # '1,200'을 숫자로 만들려면 ','삭제해야 함
                    self.tableWidget_2.setItem(j, i, item_refresh)
                elif i==6:
                    item_refresh.setData(Qt.DisplayRole, float(row[i]))
                    self.tableWidget_2.setItem(j, i, item_refresh)
                item_refresh.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tableWidget_2.setSortingEnabled(True)

        self.tableWidget_2.resizeRowsToContents()

    def load_buy_sell_list(self):
        f = open("buy_list_2.txt", 'rt', encoding='UTF-8')
        buy_list = f.readlines()
        f.close()

        row_count = len(buy_list)
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setRowCount(row_count)

        # buy list
        for j in range(len(buy_list)):
            row_data = buy_list[j]
            split_row_data = row_data.split(';')
            for i in range(len(split_row_data)):
                item = QTableWidgetItem(split_row_data[i].rstrip())
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.tableWidget_3.setItem(j, i, item)

        self.tableWidget_3.setSortingEnabled(True)
        self.tableWidget_3.resizeRowsToContents()

    def trade_stocks(self):
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        f = open("buy_list_2.txt", 'rt', encoding='UTF-8')
        buy_list = f.readlines()
        f.close()

        account = self.comboBox.currentText()

        # 추천 종목에서 매수/매도
        for index , row_data in enumerate(buy_list):
            row_data=row_data.strip('\n')  # 열 마지막에 '\n'을 삭제해야 'True'가 됨(그렇지 않으면 'True\n'과 같음)
            split_row_data = row_data.split(';')
            hoga = split_row_data[2]
            code = split_row_data[1]
            num = split_row_data[3]
            # price = split_row_data[4]
            price = 0  # 시장가 매수로 금액은 0원으로 설정

            if int(split_row_data[3]) == 0 and split_row_data[6] =='True': # 매수 조건 만족
                # num=10  일정 종목당 수량 매수
                num=str(int(200000/int(split_row_data[4])))  #일정 종목당 금액 매수
                print("trade buy in buy_list!!")
                self.kiwoom.send_order("send_order_req", "0101", account, 1, code, num, price, hoga_lookup[hoga], "")  #매수

            if int(split_row_data[3]) > 0 and split_row_data[5] =='True': # 매도 조건 만족
                print("trade sell in buy_list!!")
                self.kiwoom.send_order("send_order_req", "0101", account, 2, code, num, price, hoga_lookup[hoga], "")  #매도

            time.sleep(0.2) #send_order 주문은 1초에 5회로 제한(키움 정책), 초과 시 에러 송출/주문 무시


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
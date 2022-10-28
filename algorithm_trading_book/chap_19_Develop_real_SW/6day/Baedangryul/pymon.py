import math
import time
import sys
import webreader
import datetime
import numpy as np
from PyQt5.QtWidgets import *
from jongmok_code import *

class PyMon:
    def __init__(self):
        pass

    def calculate_estimated_dividend_to_treasury(self, code):
        estimated_dividend_yield = webreader.get_estimated_dividend_yield(code)
        
        if math.isnan(estimated_dividend_yield): # nan인 경우 처리
            estimated_dividend_yield = webreader.get_dividend_yield(code) # get_dividend_yield의 출력은 str이므로 nan이 발생하지 않음
            if estimated_dividend_yield=='': # 빈 문자인 경우 처리
                estimated_dividend_yield = 0
        
        
        current_3year_treasury = webreader.get_current_3year_treasury()
        estimated_dividend_to_treasury = float(estimated_dividend_yield) / float(current_3year_treasury)
        return estimated_dividend_to_treasury

    def get_min_max_dividend_to_treasury(self, code):
        previous_dividend_yield = webreader.get_previous_dividend_yield(code)
        three_years_treasury = webreader.get_3year_treasury()
        # print(previous_dividend_yield.keys())
        # print(three_years_treasury.keys())
        now = datetime.datetime.now()
        cur_year = now.year
        previous_dividend_to_treasury = {}

        for year in range(cur_year-5, cur_year):
            if year in previous_dividend_yield.keys() and year in three_years_treasury.keys():
                ratio = float(previous_dividend_yield[year]) / float(three_years_treasury[year])
                previous_dividend_to_treasury[year] = 0 if math.isnan(ratio) else ratio
        print(previous_dividend_to_treasury)
        if len(previous_dividend_to_treasury) > 0:
            min_ratio = min(previous_dividend_to_treasury.values())
            max_ratio = max(previous_dividend_to_treasury.values())
        else:
            min_ratio=0
            max_ratio=0

        return (min_ratio, max_ratio)
    
    def buy_check_by_dividend_algorithm(self, code):
        estimated_dividend_to_treasury = self.calculate_estimated_dividend_to_treasury(code)
        (min_ratio, max_ratio) = self.get_min_max_dividend_to_treasury(code)

        if estimated_dividend_to_treasury >= max_ratio and max_ratio !=0:
            return (1, estimated_dividend_to_treasury)
        else:
            return (0, estimated_dividend_to_treasury)

    def run_dividend(self):
        check_counter=len(code_list())
        index=1
        buy_list = []

        for code in code_list():
            print('Check: ', code, ', ', str(index), '/', str(check_counter))
            index=index+1
            time.sleep(0.5)
            try:
                ret = self.buy_check_by_dividend_algorithm(code)
            except Exception as e:
                print('Error: %s', e)

            if ret[0] == 1:
                print("Pass", ret)
                buy_list.append((code, ret[1]))
            else:
                print("Fail", ret)

        sorted_list=sorted(buy_list, key=lambda t:t[1], reverse=True)
        print(sorted_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pymon = PyMon()
    #pymon.run()
    # print(pymon.calculate_estimated_dividend_to_treasury('050860'))
    # print(pymon.get_min_max_dividend_to_treasury('216050'))
    # print(pymon.buy_check_by_dividend_algorithm('381970'))
    pymon.run_dividend()

#정적 메서드
""" class 클래스이름:
    @staticmethod
    def 메서드(매개변수1, 매개변수2):
        코드 """
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

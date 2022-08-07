#class 클래스이름:
#    def 메서드(self): 첫 번째 매개변수는 반드시 self를 지정해야 함
#        코드
class Person:
    def greeting(self):
        print('Hello')
james=Person()
james.greeting()

#특정 클래스의 인스턴스인지 확인하기, isinstance()
print( isinstance(james, Person) )

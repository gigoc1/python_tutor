class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
# print(james.hello)    # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함
# super()로 부모클래스 초기화하기, super().메서드()

class Student2(Person):
    def __init__(self):
        print('Student2 __init__')
        super().__init__()                # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장2'
 
james2 = Student2()
print(james2.school)
print(james2.hello)

#자식 클래스에서 __init__ 생략한다면, 부모 클래스 __init__ 자동으로 호출
# super() 사용하지 않아도 됨
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    pass
 
james = Student()
print(james.hello)
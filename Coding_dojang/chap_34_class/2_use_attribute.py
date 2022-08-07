#class 클래스이름:
#    def __init__(self):
#        self.속성 = 값
class Person:
    hello2='hello'
    def __init__(self):  # special method
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
        print(self.hello2)
 
james = Person()
james.greeting()    # 안녕하세요.

#인스턴스 만들때 값 받기
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
 
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    # 안녕하세요. 저는 마리아입니다.
 
print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동

#클래스의 위치/키워드 인수, 리스트/딕트 언패킹
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
 
maria = Person(*['마리아', 20, '서울시 서초구 반포동'])

class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
 
maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})

# 인스턴스는 자유롭게 속성을 추가할 수 있음
# 특정 속성만 허용하고 다른 속성은 제한할 경우, __slots__에 허용할 속성 이름을 리스트로 넣어주면 됨
# __slots__ = ['속성이름1, '속성이름2']
class Person:
    __slots__ = ['name', 'age']    # name, age만 허용(다른 속성은 생성 제한)
maria = Person()
maria.name = '마리아'  # 허용된 속성
maria.age = 20         # 허용된 속성
# maria.address = '서울시 서초구 반포동'    # 허용되지 않은 속성은 추가할 때 에러가 발생함

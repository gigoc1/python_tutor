#클래스 속성 사용하기
#class 클래스이름:
#    속성 = 값

#인스턴스 속성 사용하기
class Person:
    def __init__(self):
        self.bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')
print(james.bag)
print(maria.bag)

#비공개 클래스 속성 사용하기
#class 클래스이름:
#    __속성 = 값

#클래스와 메서드의 독스트링 사용하기
#클래스 메서드 사용하기
""" class 클래스이름:
    @classmethod
    def 메서드(cls, 매개변수1, 매개변수2):
        코드 """
class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
kdk = Person()
 
Person.print_count()    # 2명 생성되었습니다.

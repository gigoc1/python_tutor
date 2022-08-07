#def 함수이름1():
#    코드
#    def 함수이름2():
#        코드
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()
 
print_hello()

# nonlocal 지역변수
def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()

#nonlocal이 변수 찾는 순서(가장 가까운 함수부터 찾는다)
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()

#global로 전역 변수 사용하기(무조건 전역변수를 사용함)
x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x + 30
            print(x)
        C()
    B()
 
A()

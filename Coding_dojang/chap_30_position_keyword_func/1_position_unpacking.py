# 위치 인수
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
print_numbers(10,20,30)

#언패킹 사용
    #함수(*리스트)
    #함수(*튜플)
x=[10,20,30]
print_numbers(*x)

#가변인수 함수
#def 함수이름(*매개변수):
#    코드
def print_numbers1(*args):
    for arg in args:
        print(arg)
print_numbers1('kdk','lke')
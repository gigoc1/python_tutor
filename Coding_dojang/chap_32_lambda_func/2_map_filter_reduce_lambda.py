#람다 표현식에 조건부 표현식 사용하기
#lambda 매개변수들: 식1 if 조건식 else 식2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( list(map(lambda x: str(x) if x % 3 == 0 else x, a)) ) #if, else문에 : 없음

#if문이 여러개일 경우
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a)) )

#map에 객체 여러개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print( list(map(lambda x, y: x * y, a, b)) )

#filter 사용하기
#filter(함수, 반복가능한객체)
def f(x):
    return x > 5 and x < 10
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print( list(filter(f, a)) )
print( list(filter(lambda x: x>5 and x<10,a)) )

# reduce 사용하기
#: 반복 가능한 객체 각 요소를 함수로 처리한뒤, 이전결과와
# 누적해서 반환하는 함수
#from functools import reduce
#reduce(함수, 반복가능한객체)
a = [1, 2, 3, 4, 5]
from functools import reduce
print( reduce(lambda x, y: x + y, a) )
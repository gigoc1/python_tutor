fruits = {'orange', 'orange', 'cherry'}
print(fruits)

# set로 세트 만들기
print(set('apple')) #set(반복가능한 객체)
print(set(range(5)))

# 자료형의 종류 확인: type(객체)
c={}
print(type(c))
c=set()
print(type(c))

#세트는 세트안에 세트를 넣을 수 없음

#프로즌 세트는 내용을 변경할 수 없음
a=frozenset(range(10))
print(a)
#프로즌 세트는 내부에 프로즌 세트만 넣을수 있음
b=frozenset({frozenset({1, 2}), frozenset({3, 4})})
print(b)
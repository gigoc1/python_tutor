#lambda 매개변수들: 식
#lambda x: x + 10
#람다 함수를 호출할려면 변수에 할당해야함
plus_ten = lambda x: x + 10
plus_ten(1)

#람다 표현식 자체를 호출하기
#(lambda 매개변수들: 식)(인수들)
print((lambda x:x+10)(1))

#람다 표현식 안에서는 변수를 만들수 없다
# (lambda x: y = 10; x + y)(1) ; 에러 발생

#람다 표현식을 인수로 사용하기
print( list(map(lambda x: x + 10, [1, 2, 3])) )

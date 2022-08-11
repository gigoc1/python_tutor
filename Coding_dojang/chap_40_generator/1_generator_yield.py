def number_generator():
    yield 0
    yield 1
    yield 2
 
for i in number_generator():
    print(i)

# 변수 = next(제너레이터객체)
g = number_generator()
print(next(g))
print(next(g))
print(next(g))
#next(반복가능한객체, 기본값)
#next의 기본값을 지정하면, 반복이 끝나더라도 StopIteration 없이 기본값 출력
it =iter(range(3))
for i in it:
    print(i, end=' ')
print(next(it,0))
print(next(it,10))
print(next(it,10))
print(next(it,10))
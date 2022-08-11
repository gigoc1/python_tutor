# __iter__, __next__ 가진 객체: iterator protocol 지원
it = [1, 2, 3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
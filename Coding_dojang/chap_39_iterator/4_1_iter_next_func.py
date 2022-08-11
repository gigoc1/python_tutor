it=iter(range(3))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

#iter
#iter(호출가능한객체, 반복을끝낼값)
import random
it = iter(lambda : random.randint(0, 5), 2)
""" print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
 """
for i in it:
    print(i, end=' ')
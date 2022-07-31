#리스트 a, b에서 b = a로 할당하면, a와 b는 동일한 값을 가짐
#새로운 리스트로 만들려면, b = a.copy()

from re import A


a=[0,0,0,0,0]
b=a
b[2]=99
print(a, b, sep=',')

b=a.copy()
b[2]=98
print(a, b, sep=',')
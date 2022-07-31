a = [i for i in range(10)]
b=list(i for i in range(10))
print(a,b,sep=', ')
c=list(i*2 for i in range(10))
print(c)

b = [i + 5 for i in range(10) if i % 2 == 1]
print(b)

a = [i * j for j in range(2, 10) for i in range(1, 10)] #for문의 처리순서는 뒤에서 앞으로
print(a)

t=(48,76,43,62,19)
print(43 in t)
print(18 not in t)

print('The length of t(tuple): '+str(len(t)) )

hello='hello, world!'
print(len(hello))
print(hello[0], hello[-1])

l=[1,2,3,4,5]
l[0]=6
del l[4]
print(l)
print(l[1:-1])
print(l[1:5:2])

l=[0,10,20,30,40,50,60,70,80,90]
print(l[:7], l[7:])
del l[2:5]
print(l)
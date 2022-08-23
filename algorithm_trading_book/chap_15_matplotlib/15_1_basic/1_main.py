import matplotlib.pyplot as plt
x=range(0,100)
y = [v*v for v in x]
# plt.plot(x,y, 'ro')

fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
ax1.plot(x,y)
ax2.bar(x,y)
plt.show()
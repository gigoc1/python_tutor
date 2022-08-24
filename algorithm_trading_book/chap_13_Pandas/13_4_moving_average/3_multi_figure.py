import matplotlib.pyplot as plt
x=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
y=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
for i in range(len(x)):
    plt.figure()
    plt.plot(x[i],y[i])
# Show/save figure as desired.
plt.show()
# Can show all four figures at once by calling plt.show() here, outside the loop.
# 출처: https://theonly1.tistory.com/2469 [Be the only one, not the best one:티스토리]
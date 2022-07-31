import turtle as t
t.shape('turtle')
t.color('red')
t.begin_fill()
print('input n: ', end='')
n=int(input())
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.end_fill()

t.speed('fastest')
for i in range(60):
    t.circle(120)
    t.right(360/60)

t.mainloop()
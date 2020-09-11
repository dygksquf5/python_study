import turtle as t

n = 50
t.bgcolor("black")
t.color("green")
t.speed(0)

for x in range(n):
    t.circle(x*2)
    t.left(360/n)

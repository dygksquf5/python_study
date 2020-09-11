import turtle as t

# 삼각형그리기

d = 100
c = 120

for x in range(3):
    t.fd(d)
    t.lt(c)


#사각형 그리기

d = 100
c = 90

for x in range(4):
    t.fd(d)
    t.lt(c)


#원그리기

d = 50

t.circle(d)

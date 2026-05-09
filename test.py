from turtle import *
screensize(2000, 2000)
tracer(False)

m = 12

for i in range(3):
    fd(7 * m)
    rt(90)
    fd(12 * m)
    rt(90)

up()

fd(4 * m)
rt(90)
fd(6 * m)
lt(90)

down()

for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)

up()

for x in range(0, 8):
    for y in range(-12, 1):
        goto(x * m, y * m)
        dot(3, 'red')
print((4 - -80) * (72 - -6))
print((1- -12) * (8 - 0))


update()
done()
from turtle import *
screensize(2000,2000)
tracer(False)

m = 15

for i in range(4):
    fd(28 * m)
    rt(90)
    fd(26 * m)
    rt(90)

up()

fd(12 * m)
rt(90)
fd(13 * m)
lt(90)

down()

for i in range(4):
    fd(67 * m)
    rt(90)
    fd(76 * m)
    rt(90)

up()

for x in range(12, 29):
    for y in range(-26, -12):
        goto(x * m, y * m)
        dot(3, "red")
print((29 - 12) * (-12 - -26))
update()
done()
from turtle import *
screensize(2000,2000)
tracer(False)

m = 15

rt(45)

for i in  range(7):
    fd(5 * m)
    rt(45)
    fd(10 * m)
    rt(135)

up()

for x in range(0, 100):
    for y in range(-14, 0):
        goto(x * m, y * m)
        dot(3, "red")

update()
done()

print("Ответ: 27")
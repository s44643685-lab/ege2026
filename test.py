from turtle import *
screensize(2000, 2000)
tracer(False)
# дз 21892
# m = 15
#
# rt(90)
#
# for i in range(7):
#     rt(45)
#     fd(11 * m)
#     rt(45)
#
# up()
#
# for x in range(-15, 1):
#     for y in range(-8, 9):
#         goto(x * m, y * m)
#         dot(3, "red")
# update()
# done()
#
# # дз 21892
m = 12

for i in range(3):
    fd(39 * m)
    rt(90)
    fd(48 * m)
    rt(90)

up()

fd(27 * m)
rt(90)
fd(24 * m)
lt(90)

down()

for i in range(3):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)

up()

for x in range(-17, 13):
    for y in range(28, 47):
        goto(x * m, y * m)
        dot(3, "red")
print (((13 - -17)+(47 - 28)) * 2)
update()
done()

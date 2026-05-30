# from turtle import *
# screensize(2000,2000) #увеличение экрана
# tracer(False) #отключает анимацию
# forward(100) #движение вперед
# back(50) #движение назад
# left(90) #движение влево
# right(90) #движение вправо
# up() #поднять перо
# down() #опустить перо
# m = 20
# left(90)
#
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(18 * m)
#     rt(90)
#
# up()
#
# fd(5 * m)
# rt(90)
# fd(7 * m)
# lt(90)
#
# down()
#
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(7 * m)
#     rt(90)
#
# up()
# for x in range(7, 15):
#     for y in range(5, 11):
#         goto(x * m, y * m)
#         dot(3,"red")
# print(19 * 11 + (15 - 7) * (16 - 8) - (15 - 7) * (11 - 5))

# update() #обновляет экран
# done() #рисунок остается на экране

# дз 1 9737
# m = 20
#
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(18 * m)
#     rt(90)
#
# up()
#
# fd(5 * m)
# rt(90)
# fd(7 * m)
# lt(90)
#
# down()
#
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(7 * m)
#     rt(90)

# дз 29959
from turtle import *
screensize(2000,2000)
tracer(False)

m = 10

for i in range(3):
    forward(32 * m)
    right(90)
    forward(38 * m)
    right(90)

up()

forward(25 * m)
right(90)
forward(21 * m)
left(90)

down()

for i in range(3):
    forward(29 * m)
    right(90)
    back(18 * m)
    right(90)

up()

for x in range(0, 8):
     for y in range(-35, -16):
         goto(x * m, y * m)
         dot(3,"red")
print(33 * 39 + 19 * 30 - (8 * 19))
update()
done()

# дз 28693
# from turtle import *
# screensize(2000,2000)
# tracer(False)
# m = 20
#
# for i in range(2):
#     fd(5 * m)
#     lt(270)
#     bk(8 * m)
#     lt(270)
#
# up()
#
# fd(2 * m)
# rt(90)
# bk(3 * m)
# lt(90)
#
# down()
#
# for i in range(3):
#     fd(8 * m)
#     lt(270)
#     fd(4 * m)
#     lt(270)
#
# up()
#
# fd(4 * m)
# rt(90)
# bk(2 * m)
#
# down()
#
# for i in range(3):
#     fd(5 * m)
#     rt(90)
#     fd(7 * m)
#     rt(90)
#
# up()
#
# for x in range(0, 14):
#      for y in range(-3, 9):
#          goto(x * m, y * m)
#          dot(3,"red")
#
# update()
# done()
from turtle import *
screensize(2000,2000) #увеличение экрана
tracer(False) #отключает анимацию
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

update() #обновляет экран
done() #рисунок остается на экране

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

# дз 2 9775

m = 20

for i in range(2):
    forward(13 * m)
    right(90)
    forward(20 * m)
    right(90)

up()

forward(8 * m)
right(90)
back(3 * m)
left(90)

down()

for i in range(2):
    forward(16 * m)
    right(90)
    forward(8 * m)
    right(90)

update()
done()
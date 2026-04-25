# ? boolean / bool / логические тип
from math import ceil

bool_1 = True
print(bool_1, type(bool_1))
bool_2 = False
print(bool_2, type(bool_2))

# ? логические операиторы
print(5 > 3) # больше
print(4 >= 2) # больше или равно
print(3 < 1) # меньше
print(10 <= 3) # меньше или равно
print(10 != 3) # не равно
print(10 == 3) # равно

# ? условные операторы
num = -10
if num > 0:
    print("Число положительное")
else:
    print("Число отрицателное")

 # ? условные операторы
num = 5
if num % 2 == 0:
     print("Число четное")
else:
    print("Число нечетное")

# ? if-elif-else
color = "green"
if color == "green":
    print("Едим")
elif color == "red":
    print("Стой")
else:
    print("Ждем")

age = 18
if age >= 18:
    print("проходи в кино")
else:
    print("не проходи")

a = 20
b = 15
if a > b:
    print("а больше")
elif a < b:
    print("а меньше")
else:
    print("а равно b")

day = "mon"
if day == "sun":
    print("выходной")
elif day == "sut":
    print("выходной")
else:
    print("будний")

x = 10
y = 17
if x > 0 and y > 0:
    print("первая четверть")
elif x > 0 and y < 0:
    print("вторая четверть")
elif x < 0 and y < 0:
    print("третья")
elif x > 0 and y < 0:
    print("четвертая")
else:
    print("невозможно определить")

# ()
# not - нет
# and - и
# or - или
from math import*
# # дз 7 1165
#  k = 2
#  V = 18
#  n = 1.5
#  i = 1 / 6

# # дз 11 3889
# L = 115
# N = 10 + 1020
# i = ceil(log2(N))
# I = L * i / 8
# V = I * 16384 / 2**10
# print(V)

# # 11
# N = 27 + 10
# i = ceil(log2(N))
# n = 3548
# V = 12
# I = ceil(V * 2**10 / n)
# print(I)
# L = I * 8 / i
# print(L)
# print(ceil(floor(L) * i / 8))
# print(ceil(ceil(L) * i / 8))

# # 11
# L = 172
# V = 54
# n = 356984
# I = ceil(V * 2**20 / n)
# print("I", I)
# i = I * 8 / L
# print("i" , i)
# print(ceil(L * floor(i) / 8))
# print(ceil(L * ceil(i) / 8))

# # 7
# k = 2
# n = 48 * 1000
# p = 13
# t = 42 * 60 + 20
# i = 34
# V = k * n * t * i + p * 110 * 2**13
# q = 314572800
# t_q = V / q
# print(t_q)

V1 = 2560 * 1440 * 22
V2 = 1920 * 1080 * 20
print((V1 - V2) * 130 / 2**13)




# ? boolean / bool / логические тип
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


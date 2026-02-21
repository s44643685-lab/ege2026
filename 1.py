# * print() выводит данные на экран
print ("Hello World") # двойные кaвычки
print ("Hello World") # одинарные кaвычки

# * переменные
name = "Алекс"
print(name)

# * меняем значение переменной
name = "Ваня"
print(name)

# * создание нескольких переменных
num1,num2 = 5, 10
num3 = 15
num4 = 20

# ! Правила наиминование переменных
# * только латинские символы a-z A-Z
# * цифры, но не на первой позиции
# * разрешены символы _
# * нельзя использовать зарезервированные имена

# * snake_case
ticket_price = 500

# * camelCase
ticketPrice = 500


# ? Типы данных - у каждого свое предназначение
# * integer / int / целое число
my_int = 10
print(my_int, type(my_int))

big_number = 123_456_789
print(big_number,type(big_number))

# * float / float / дробные числа
my_float = 36.6
print(my_float, type(my_float))
print(0.1 + 0.2) # ! 0.300000004

big_float = 2.5e6 # * 2.5 * 10^6
print(big_float, type(big_float))

# ? Операцие с числами
x = 10
y = 5
print(x + y) # * сложение
print(x - y) # * вычитание
print(x * y) # * умножение
print(x / y) # * обычное деление - всегда float
print(y ** x) # * возведение в степень
print(13 % 5) # * остаток от деление 13 % 5 = 2 (3 остаток)
print(13 // 5) # * целочисленное деление 13 // 5 = 2
print((x + y) * x)
# ! print(5 / 0) на ноль делить нельзя

# * string / str / строки
company = 'Apple'
name = "Алекс"
long_text = """Это длинный
 текст"""
print ("Говорит - 'Алекс'")
print(company, type(company))

# * Операции со строками
name1, surname = "Иван", "Иванович"
print(name + surname)
print(name * 5)

# * boolean / bool / логический тип данных
bool1, bool2 = True, False
print(bool1, type(bool1))
print(5 > 2)
print(5 < 2)

# ? задачи
a,b,c = 1,2,3
a,b,c = c,a,b
print(a,b,c)

a = 7
b = 3
print(a + b)

x,y = 15,4
print(x - y)

m,n = 6,5
print(m * n)

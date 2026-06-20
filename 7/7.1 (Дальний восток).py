from math import*
t = 75
k = 1
n = 48000
i = 16
I = i * n * t * k
I2 = ceil(I / 2**13)
print(I2)
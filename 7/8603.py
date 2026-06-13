from math import*
k = 4
t = 3 * 60
n = 48000
i = 16
I = k * t * n * i
q = 3200
t2 = (I // q) / 3600
print(t2)
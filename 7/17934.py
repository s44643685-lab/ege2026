from math import*
N = 510 + 10
i = ceil(log2(N))
L = 99
I = floor((L * i) / 8)
n = 4322
V = 543 * 2**10
I2 = floor(V / n)
V2 = I2 - I
print(V2)

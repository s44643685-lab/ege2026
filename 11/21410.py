from math import*
L = 257
V = 33 * 1024 * 1024
n = 295740

I = floor(V / n) * 8
i = floor(I / L)
N = 2**i
print(N)

print(ceil(i * L / 8) * n <= V)
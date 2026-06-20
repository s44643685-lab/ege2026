from math import*
L = 200
n = 85536
V = 9 * 2**20
I = ceil((V / n) * 2**3)
i = ceil(I / L)
N = 2**i
print(N)


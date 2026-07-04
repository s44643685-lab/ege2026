from math import*
h = 1536
w = 1024
N = 4092
i = ceil(log2(N))
q = 288
t = 4 * 60

V = h * w * i * 150
I = q * 2**13 * t
V2 = V - I
V3 = (V2 / V) * 100
print(V3)
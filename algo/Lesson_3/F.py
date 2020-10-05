import math

[vp, vf] = list(map(int, input().split()))
a = float(input())

EPS = 10 ** (-10)
STEPS = math.ceil(math.log2(1 / EPS))
PHI = (1 + 5 ** 0.5) / 2


def funk(x, v1=vp, v2=vf, border=a):
    return (x ** 2 + (1 - border) ** 2) ** 0.5 / v1 + ((1 - x) ** 2 + border ** 2) ** 0.5 / v2


left = 0
right = 1

m2 = right / PHI
m1 = m2 / PHI

f1 = funk(m1)
f2 = funk(m2)

for _ in range(STEPS):
    if f1 < f2:
        right = m2
        m2 = m1
        f2 = f1
        m1 = left + (right - left) * (1 - 1 / PHI)
        f1 = funk(m1)
    else:
        left = m1
        m1 = m2
        f1 = f2
        m2 = left + (right - left) / PHI
        f2 = funk(m2)

print(right)

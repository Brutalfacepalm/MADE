import math

c = float(input())

EPS = 10 ** (-6)


def func(x):
    return x ** 4 + x


left = 0
right = 1
while func(right) < c:
    left = right
    right *= 2
steps = math.ceil(math.log2((right - left) / EPS))

for _ in range(steps):
    m = (left + right) / 2
    if func(m) < c:
        left = m
    else:
        right = m

print(round(right ** 2, 6))

import sys

n = int(input())
a_n = sorted(list(map(int, input().split())))
k = int(input())


def bound(arr, x):
    lt = -1
    rt = len(arr)
    while lt < rt - 1:
        m = (lt + rt) // 2
        if x <= arr[m]:
            rt = m
        else:
            lt = m
    return rt


s = []

for _ in range(k):
    [l, r] = list(map(int, sys.stdin.readline().split()))

    left = bound(a_n, l)
    right = bound(a_n, r + 1)

    s.append(str(right - left))

print(' '.join(s))

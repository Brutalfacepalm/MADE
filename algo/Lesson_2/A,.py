from collections import deque

N = int(input())
army = list(map(int, input().split()))
m = int(input())
i_j_k = [(list(map(int, input().split()))) for _ in range(m)]


def for_dooku(a, lt, rt, k):
    if len(a) <= 1:
        return a[0]
    x = a[len(a) // 2]
    left_a = deque()
    right_a = deque()
    while lt <= rt:
        if a[lt] < x:
            left_a.append(a[lt])
            lt += 1
        elif a[lt] > x:
            right_a.append(a[lt])
            lt += 1
        else:
            right_a.appendleft(x)
            lt += 1
    if k <= len(left_a):
        left_a = for_dooku(left_a, 0, len(left_a) - 1, k)
        return left_a
    else:
        right_a = for_dooku(right_a, 0, len(right_a) - 1, k - len(left_a))
        return right_a


for [i, j, ks] in i_j_k:
    iq_k = for_dooku(army, i - 1, j - 1, ks)
    print(iq_k)

# Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания.
#
# Входные данные
# В первой строке входного файла содержится число N (1 ≤ N ≤ 100 000) —
# количество элементов в массиве. Во второй строке находятся N целых чисел, по модулю не превосходящих 109.
#
# Выходные данные
# В выходной файл надо вывести этот же массив в порядке неубывания,
# между любыми двумя числами должен стоять ровно один пробел.

from collections import deque


def merge(l, r):
    c = deque()
    while l and r:
        if l[0] < r[0]:
            c.append(l.popleft())
        elif l[0] > r[0]:
            c.append(r.popleft())
        else:
            c.append(l.popleft())
            c.append(r.popleft())
    if not l and r:
        c.extend(r)
    elif not r and l:
        c.extend(l)

    return c


def split_array(a):
    n = len(a)
    if n == 1:
        return a
    else:
        l = deque(list(a)[:n // 2])
        r = deque(list(a)[n // 2:])

        l = split_array(l)
        r = split_array(r)
        return merge(l, r)


N = int(input())
a = deque(map(int, input().split()))

c = ' '.join(map(str, split_array(a)))

print(c)

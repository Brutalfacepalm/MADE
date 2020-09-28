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

import random


def qsort(a, l, r):
    if l >= r:
        return a
    x = a[random.randint(l, r)]
    i, j = l, r

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    qsort(a, l, j)
    qsort(a, i, r)

    return a

N = int(input())
a = list(map(int, input().split()))

print(' '.join(map(str, qsort(a, 0, len(a) - 1))))

# Напишите программу, которая для заданного массива  находит количество пар (i, j) таких,
# что i < j и ai > aj.
#
# Входные данные
# Первая строка входного файла содержит натуральное число n (1 ≤ n ≤ 500 000) — к
# оличество элементов массива. Вторая строка содержит n попарно различных элементов массива A
# (0 ≤ ai ≤ 106).
#
# Выходные данные
# В выходной файл выведите одно число — ответ на задачу.


from collections import deque


from collections import deque


def merge(l, r, count):
    c = deque()

    while l and r:
        if l[0] < r[0]:
            c.append(l.popleft())
        elif l[0] > r[0]:
            # c.append(r.popleft())
            count += len(l)
        else:
            c.append(l.popleft())
            c.append(r.popleft())
    if not l and r:
        c.extend(r)
    elif not r and l:
        c.extend(l)

    return c, count


def split_array(a, count):
    n = len(a)
    if n == 1:
        return a, count
    else:
        l = deque(list(a)[:n // 2])
        r = deque(list(a)[n // 2:])

        l, count = split_array(l, count)
        r, count = split_array(r, count)
        return merge(l, r, count)


N = int(input())
a = deque(map(int, input().split()))

count = 0
c, count = split_array(a, count)


print(count)
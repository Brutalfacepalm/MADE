from collections import deque

# 6
# Louis IX
# Zod VIII
# And VIII
# Mark XLIX
# Philippe II
# Philip II

import random

kings = int(input())
a = [input().split() for _ in range(kings)]

digs = {'XL': '40',
        'L': '50',
        'XXX': '30',
        'XX': '20',
        'IX': '9',
        'X': '10',
        'IV': '4',
        'V': '5',
        'III': '3',
        'II': '2',
        'I': '1'}


def convert_roman_digs(roman_digs, digs):
    for d in digs:
        if d in roman_digs:
            roman_digs = roman_digs.replace(d, ' ' + digs[d])
    return [str(sum(map(int, roman_digs.split()))).rjust(2, '0')]


def sort_kings(a, k):
    kings = {}
    king_rank = list(map(lambda x: [v*10**(2*i+2) for i,v in enumerate(x[::-1][1:])]+[x[-1]], k))
    for i, king in enumerate(a):
        kings[' '.join(king)] = sum(king_rank[i])


    def qsort(a, l, r):
        if l >= r:
            return a
        x = a[random.randint(l, r)][1]
        i, j = l, r

        while i <= j:
            while a[i][1] < x:
                i += 1
            while a[j][1] > x:
                j -= 1

            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        qsort(a, l, j)
        qsort(a, i, r)

        return a

    kings = list(map(list, kings.items()))

    kings = qsort(kings, 0, len(kings) - 1)

    return kings


l = max([len(i[0]) for i in a])
a_splited = list(map(lambda x: list(map(lambda z: ord(z)-65, x[0])) + [0 for _ in range(l - len(x[0]))] + [int(convert_roman_digs(x[1], digs)[0])], a))


[print(king[0]) for king in sort_kings(a, a_splited)]

# print(10e25)

# [print(f'{s}: ', chr(s)) for s in range(65,123)]



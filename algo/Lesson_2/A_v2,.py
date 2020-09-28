import random

N = int(input())
army = list(map(int, input().split()))
m = int(input())
i_j_k = [(list(map(int, input().split()))) for _ in range(m)]


def for_dooku(a, lt, rt, k):
    if lt >= rt:
        return
    xi = random.randint(lt, rt)
    x = a[xi]
    i, j = lt, rt

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if k <= i:
        for_dooku(a, lt, j, k)
    else:
        for_dooku(a, i, rt, k)


presets = {}

for [i_army, j_army, ks] in i_j_k:
    i_j = ' '.join(map(str, [i_army, j_army]))
    if i_j in presets:
        clones_i_j = presets[i_j]
        for_dooku(clones_i_j, 0, len(clones_i_j) - 1, ks)
        presets[i_j] = clones_i_j
        print(clones_i_j[ks - 1])
    else:
        clones_i_j = army[i_army - 1: j_army]
        for_dooku(clones_i_j, 0, len(clones_i_j) - 1, ks)
        presets[i_j] = clones_i_j
        print(clones_i_j[ks - 1])

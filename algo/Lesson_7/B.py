import math

[n, m, a1] = list(map(int, input().split()))
[u0, v0] = list(map(int, input().split()))

MOD = 16714589
K = 23
B = 21563
K_u = 17
B_u = 751
K_v = 13
B_v = 593


def mod(value, mod):
    if value >= mod or value < 0:
        value %= mod
        return value
    return value


def search_min(u, v, s_m):
    if u < v:
        l, r = u, v
    else:
        l, r = v, u

    if u == v:
        min_l_r = s_m[l - 1][0]
        return [u, v, min_l_r]

    k_pow = _k_pow[r - l]

    l_r = r - pows_2[k_pow]

    min_l = s_m[l - 1][k_pow]
    min_r = s_m[l_r][k_pow]
    if min_l < min_r:
        return [u, v, min_l]
    else:
        return [u, v, min_r]


if n > 1:
    MAX_K_POW = int(math.ceil(math.log2(n)))

    _k_pow = [int(math.trunc(math.log2(i))) for i in range(1, n + 1)]
    pows_2 = [2 ** i for i in list(set(_k_pow))]

    sparse_matrix = [[math.inf for _ in range(MAX_K_POW)] for _ in range(n)]


    def get_ai(x):
        return mod(K * x + B, MOD)


    for k in range(MAX_K_POW):
        for i in range(n):
            if k == 0:
                if i == 0:
                    sparse_matrix[i][k] = a1
                else:
                    sparse_matrix[i][k] = get_ai(sparse_matrix[i - 1][k])
            else:
                r = i + pows_2[k - 1]
                if r > n - 1:
                    r = n - 1
                if sparse_matrix[i][k - 1] < sparse_matrix[r][k - 1]:
                    min_ = sparse_matrix[i][k - 1]
                else:
                    min_ = sparse_matrix[r][k - 1]
                sparse_matrix[i][k] = min_

    u_v_r = search_min(u0, v0, sparse_matrix)

    for i in range(1, m):
        u = mod(K_u * u_v_r[0] + B_u + u_v_r[2] + 2 * i, n) + 1
        v = mod(K_v * u_v_r[1] + B_v + u_v_r[2] + 5 * i, n) + 1
        u_v_r = search_min(u, v, sparse_matrix)

    print(' '.join(map(str, u_v_r)))
else:
    # sparse_matrix = [[a1]]
    print(' '.join(map(str, [u0, v0, a1])))


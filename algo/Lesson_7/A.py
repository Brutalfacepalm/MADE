[n, x, y, a0] = list(map(int, input().split()))
[m, z, t, b0] = list(map(int, input().split()))

a = [a0]
c = []
sum_l_r = 0

MOD_2_16 = 2 ** 16
MOD_2_30 = 2 ** 30


def mod(value, mod_2_n):
    if value >= mod_2_n or value < 0:
        value %= mod_2_n
        return value
    return value


pre_sum = [a0]

for i in range(1, n):
    ai = mod(x * a0 + y, MOD_2_16)
    pre_sum.append(pre_sum[i - 1] + ai)
    a0 = ai


def get_sum(l, r):
    if l == r or l == 0:
        sum_i = pre_sum[r]
    else:
        sum_i = pre_sum[r] - pre_sum[l - 1]
    return sum_i


while m:
    b1 = mod(b0 * z + t, MOD_2_30)
    c0 = mod(b0, n)
    c1 = mod(b1, n)
    if c1 < c0:
        sum_l_r += get_sum(c1, c0)
    else:
        sum_l_r += get_sum(c0, c1)
    b0 = mod(b1 * z + t, MOD_2_30)

    m -= 1

print(sum_l_r)
print(pre_sum[0])
print(pre_sum[1])
print(pre_sum[2])

# 4 1 2 3
# 4 1 -1 4


# 10000000 1 2 3
# 3 1 -1 4

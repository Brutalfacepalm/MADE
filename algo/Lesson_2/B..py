N_MAX = 100
cnt = [0 for _ in range(N_MAX + 1)]

a = list(map(int, input().split()))
for i in a:
    cnt[i] += 1
a_sorted = [' '.join(map(str, [i for _ in range(v)])) for i, v in enumerate(cnt) if v > 0]

print(' '.join(a_sorted))

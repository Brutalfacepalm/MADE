[n, m, k] = list(map(int, input().split()))
strings = [input() for _ in range(n)]

LATIN_BEGIN = 97
LATIN_ALPHABET = 26

for ki in range(k):
    string = [(ord(s[-(1 + ki)]) - LATIN_BEGIN, i) for i, s in enumerate(strings)]
    cnt = [[[], 0] for _ in range(LATIN_ALPHABET)]
    for i in string:
        cnt[i[0]][1] += 1
        cnt[i[0]][0].append(i[1])
    p = []
    [p.extend(v[0]) for i, v in enumerate(cnt) if v[1] > 0]
    strings = [strings[i] for i in p]

print('\n'.join(strings))

[n, m] = list(map(int, input().split()))
s = input()
t = input()


def counter(s):
    r = {}
    s = list(s)
    s_set = list(set(s))
    for i in s_set:
        r[i] = s.count(i)
    return r


def substruct_dict(d1, d2):
    for i in d1:
        if i not in d2 or d1[i] > d2[i]:
            return False
    return True


cnt_t = counter(t)
cnt = 0
i = 0
j = 1
while i < n:
    substring = s[i:j]
    substring_cntr = counter(substring)
    check = substruct_dict(substring_cntr, cnt_t)
    if check:
        cnt += len(substring)
        while j <= n:
            j += 1
            next_letter = s[j - 1:j]
            if next_letter in cnt_t:
                if next_letter in substring_cntr:
                    if cnt_t[next_letter] < substring_cntr[next_letter] + 1:
                        substring_cntr[s[i: i + 1]] -= 1
                        i += 1
                        j -= 1
                        continue
                else:
                    substring_cntr[next_letter] = 0
            else:
                i = j
                j += 1
                break
            substring_cntr[next_letter] += 1
            cnt += sum(substring_cntr.values())

    else:
        i += 1
        if i >= j:
            j += 1

print(cnt)

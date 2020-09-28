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
    substr = s[i:j]
    substr_cntr = counter(substr)
    substruct_cnt = substruct_dict(substr_cntr, cnt_t)
    if substruct_cnt:
        cnt += len(substr)
        while j <= n:
            j += 1
            update_substr = s[j - 1:j]
            if update_substr in cnt_t:
                if update_substr in substr_cntr:
                    if cnt_t[update_substr] < substr_cntr[update_substr] + 1:
                        substr_cntr[s[i: i + 1]] -= 1
                        i += 1
                        j -= 1
                        continue
                else:
                    substr_cntr[update_substr] = 0
            else:
                i = j
                j += 1
                break
            substr_cntr[update_substr] += 1
            cnt += sum(substr_cntr.values())

    else:
        i += 1
        if i >= j:
            j += 1

print(cnt)

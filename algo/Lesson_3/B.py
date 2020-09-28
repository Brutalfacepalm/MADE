n = int(input())
a_n = sorted(list(map(int, input().split())))

k = int(input())


def sorted_arr(a):
    return a[1]


a_k = [list(map(int, input().split())) for _ in range(k)]


# a_k.sort(key=lambda x: x[0])
# a_k.sort(key=lambda x: x[1], reverse=True)
#
# print(a_k)

def search_bound(arr, k):
    lt = 0
    rt = len(a_k)
    while rt - lt > 1:
        m = (rt + lt) // 2
        if k < arr[m]:
            rt = m
        elif k > arr[m]:
            lt = m
        else:
            rt = m
            lt = m
            break
    if rt - lt == 1:
        if arr[rt] > k:
            if arr[lt] >= k:
                if arr[lt] > k:
                    answer = lt + 1
                else:
                    answer = lt
            else:
                answer = rt
        else:
            answer = rt + 1
    else:
        answer = lt
    return answer

s = []
for [l, r] in a_k:
    left = search_bound(a_n, l)
    right = search_bound(a_n, r + 1)

    s += [str(right - left)]

print(' '.join(s))

# 5
# 10 1 10 3 4
# 4
# 1 10
# 2 9
# 3 4
# 2 2

[n, k] = list(map(int, input().split()))
a_n = list(map(int, input().split()))
a_k = list(map(int, input().split()))


for k in a_k:
    left = 0
    right = len(a_k) - 1
    while right - left > 1:
        m = (right + left) // 2
        if k < a_n[m]:
            right = m
        elif k > a_n[m]:
            left = m
        else:
            right = m
            left = m
            break
    if right - left == 1:
        if a_n[right] > k:
            if abs(a_n[right] - k) < abs(a_n[left] - k):
                print(a_n[right])
            else:
                print(a_n[left])
        else:
            print(a_n[right])
    else:
        print(a_n[left])

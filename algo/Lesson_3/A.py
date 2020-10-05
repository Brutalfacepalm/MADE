[n, k] = list(map(int, input().split()))
a_n = list(map(int, input().split()))
a_k = list(map(int, input().split()))


for k in a_k:
    left = 0
    right = n - 1

    while right - left > 1:
        m = (left + right) // 2
        if k <= a_n[m]:
            right = m
        else:
            left = m

    right_elem = a_n[right]
    left_elem = a_n[left]

    if right_elem <= k:
        print(right_elem)
    elif left_elem >= k:
        print(left_elem)
    else:
        if abs(right_elem - k) < abs(left_elem - k):
            print(right_elem)
        else:
            print(left_elem)

# 5 5
# 1 3 5 7 9
# 2 4 8 1 6

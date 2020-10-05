import math

[n_lines, k_homes] = list(map(int, input().split()))
clotheslines = sorted([int(input()) for _ in range(n_lines)])


def check_length(cl, d, homes):
    for line in cl:
        homes -= line // d
    if homes <= 0:
        return True
    else:
        return False


min_length = clotheslines[-1] // k_homes
max_length = clotheslines[-1] + 1
steps = math.ceil(math.log2((max_length - min_length)))

if n_lines > 1 and k_homes > 1:
    for _ in range(steps):
        length = (max_length + min_length) // 2
        if check_length(clotheslines, length, k_homes):
            min_length = length
        else:
            max_length = length

print(min_length)

# print(max_length)

# 4 11
# 802
# 743
# 457
# 539


# 4 280
# 799
# 743
# 279
# 539


# 4 10
# 10
# 10
# 10
# 10


# 1 10
# 5

# 2 10
# 5
# 5

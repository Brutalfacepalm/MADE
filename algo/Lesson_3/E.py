import math

[n, x, y] = list(map(int, input().split()))


def check_time(n_copies, xerox_1, xerox_2, time):
    xerox_1_copies = time // xerox_1
    xerox_2_copies = time // xerox_2
    n_copies -= xerox_1_copies + xerox_2_copies

    if n_copies <= 0:
        return True
    else:
        return False


min_time = 0
max_time = max([x, y]) * n
steps = math.ceil(math.log2(max_time)) + 1

for _ in range(steps):
    t = (max_time + min_time) // 2

    if check_time(n - 1, x, y, t - min([x, y])):
        max_time = t
    else:
        min_time = t

print(max_time)

# 4 1 1
# 3

# 5 1 2
# 4

# 3 1 10
# 3

# 4 3 4
# 9

# 10 3 4
# 19

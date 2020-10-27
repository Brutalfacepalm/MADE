from collections import namedtuple

[n, m] = list(map(int, input().split()))
cell = namedtuple('cell', ['key', 'value'])
turtles_field = [list(map(lambda x: cell('', int(x)), input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if j == 0 and i == 0:
            pass
        elif j == 0 and i > 0:
            coins = turtles_field[i - 1][j].value + turtles_field[i][j].value
            key = turtles_field[i - 1][j].key + 'D'
            turtles_field[i][j] = cell(key, coins)

        elif j > 0 and i == 0:
            coins = turtles_field[i][j - 1].value + turtles_field[i][j].value
            key = turtles_field[i][j - 1].key + 'R'
            turtles_field[i][j] = cell(key, coins)

        else:
            coins_r = turtles_field[i][j - 1].value + turtles_field[i][j].value
            coins_d = turtles_field[i - 1][j].value + turtles_field[i][j].value

            if coins_d < coins_r:
                key = turtles_field[i][j - 1].key + 'R'
                coins = coins_r
            else:
                key = turtles_field[i - 1][j].key + 'D'
                coins = coins_d

            turtles_field[i - 1][j - 1] = None

            if i == n - 1:
                turtles_field[i][j - 1] = None

            if j == m - 1:
                turtles_field[i - 1][j] = None

            turtles_field[i][j] = cell(key, coins)
        if i > 1:
            turtles_field[i - 2] = None
            if j == m - 1:
                turtles_field[i - 1] = None

print(turtles_field[-1][-1].value)
print(turtles_field[-1][-1].key)

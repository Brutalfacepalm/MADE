from sys import stdin, stdout

SEPARATOR = "\n"
UNICODE = "utf-8"

n = int(input())
a = list(map(int, input().split()))


class Fenwick:
    def __init__(self):
        pass

    def _f_i(self):
        pass

    def set(self, i, x):
        pass

    def summ(self, i, j):
        pass


rsq = Fenwick()

for cmd in stdin.buffer.read().splitlines():
    cmd = cmd.decode(UNICODE).split()

    if len(cmd) > 0:
        i = cmd[1]
        x = cmd[2]
        command = cmd[0]
        if command == 'set':
            rsq.set(i, x)
        if command == 'sum':
            j = x
            stdout.buffer.write((rsq.summ(i, j) + SEPARATOR).encode(UNICODE))
    else:
        break
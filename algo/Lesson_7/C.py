from sys import stdin, stdout

SEPARATOR = "\n"
UNICODE = "utf-8"

n = int(input())
a = list(map(int, input().split()))


class Fenwick:
    def __init__(self, n, a):
        self.n = n
        self.body = a
        self.t = [0 for _ in range(self.n)]

    def _f_i(self, i):
        return i & (i + 1)

    def _mod(self, i, x):
        while i < self.n:
            self.t[i] += x
            i = i | (i + 1)

    def set(self, i, x):
        d = x - self.body[i]
        self.body[i] = x
        self._mod(i, d)

    def summ(self, i, j):
        r_j = 0
        while j >= 0:
            r_j += self.t[j]
            j = self._f_i(j) - 1

        r_i = 0
        while i >= 0:
            r_i += self.t[i]
            i = self._f_i(i) - 1
        r = r_j - r_i
        return r


rsq = Fenwick(n, a)

for cmd in stdin.buffer.read().splitlines():
    print(cmd)
    cmd = cmd.decode(UNICODE).split()
    if len(cmd) > 0:
        i = cmd[1]
        x = cmd[2]
        command = cmd[0]
        if command == 'set':
            rsq.set(i, x)
        if command == 'sum':
            j = x
            stdout.buffer.write((str(rsq.summ(i, j)) + SEPARATOR).encode(UNICODE))
    else:
        break

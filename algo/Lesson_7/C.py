from sys import stdin, stdout

SEPARATOR = "\n"
UNICODE = "utf-8"


class Fenwick:
    def get_body(self, n, a):
        self.n = n
        self.body = a
        self.t = [0 for _ in a]
        for i, v in enumerate(self.body):
            self.t[i] = self._t_i(self._f_i(i), i, self.body)

    def _f_i(self, i):
        return i & (i + 1)

    def _t_i(self, fi, i, a):
        r = 0
        while fi <= i:
            r += a[fi]
            fi += 1
        return r

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

        r_i = - self.body[i]
        while i >= 0:
            r_i += self.t[i]
            i = self._f_i(i) - 1
        r = r_j - r_i
        return r


rsq = Fenwick()

inputs = []
for cmd in stdin.buffer:
    cmd = cmd.strip().decode(UNICODE).split()
    if cmd:
        inputs.append(cmd)
    else:
        break

for inpt, cmd in enumerate(inputs):
    if inpt == 0:
        n = int(cmd[0])
    elif inpt == 1:
        a = list(map(int, cmd))
        rsq.get_body(n, a)
    else:
        i = int(cmd[1])
        x = int(cmd[2])
        command = cmd[0]
        if command == 'set':
            rsq.set(i - 1, x)
        if command == 'sum':
            j = x
            r = rsq.summ(i - 1, j - 1)
            stdout.buffer.write((str(r) + SEPARATOR).encode(UNICODE))

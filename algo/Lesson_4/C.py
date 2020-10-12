from sys import stdout, stdin
from io import IOBase, BytesIO
from os import read, write, fstat

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self, size: int = ...):
        while self.newlines == 0:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


stdin, stdout = IOWrapper(stdin), IOWrapper(stdout)
input = lambda: stdin.readline().rstrip("\r\n")


class Deque:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.size = 0
        self.capacity = 1
        self.body = [None] * self.capacity

    def push(self, element):
        if self.size >= self.capacity:
            self.ensure_capacity()
            self.begin = 0
            self.end = self.size

        if self.end >= self.capacity > self.size:
            self.end -= self.capacity

        self.body[self.end] = element
        self.end += 1
        self.size += 1

    def pop(self):
        operand = self.body[self.begin]
        self.body[self.begin] = None
        self.size -= 1
        self.begin += 1

        if self.size <= self.capacity // 4:
            self.decline_capacity()

        if self.size == 0:
            self.begin = 0
            self.end = 0
            self.size = 0
            self.capacity = 1
            self.body = [None] * self.capacity

        if self.begin >= self.capacity:
            self.begin -= self.capacity

        return operand

    def ensure_capacity(self):
        if self.begin < self.end:
            self.body = self.body[self.begin:self.end] + [None] * self.capacity
        else:
            begin = self.body[:self.end]
            end = self.body[self.begin:(self.begin + self.size - self.end)]
            capacity = [None] * self.capacity
            self.body = end + begin + capacity

        self.capacity *= 2

    def decline_capacity(self):
        if self.begin < self.end:
            self.body = self.body[self.begin:self.end] + [None] * (self.capacity // 4)
        else:
            begin = self.body[:self.end]
            end = self.body[self.begin:(self.begin + self.size - self.end)]
            capacity = [None] * int(self.capacity // 4)

            self.body = begin + end + capacity

        self.capacity = int(self.capacity // 2)
        self.begin = 0
        self.end = self.size


dq = Deque()

m = int(input())

for _ in range(m):
    cmd = input().split()

    if cmd[0] == '+':
        dq.push(int(cmd[1]))
    else:
        print(str(dq.pop()))

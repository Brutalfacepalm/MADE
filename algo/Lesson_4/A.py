import sys


class Stack:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.body = self.__create__()

    def __create__(self):
        return [None] * self.capacity

    def add(self, element):
        self.body[self.size] = element
        self.size += 1
        if self.size > self.capacity // 2:
            self.body += [None] * self.capacity
            self.capacity *= 2

    def remove_last(self):
        self.body[self.size - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 4:
            self.capacity = int(self.capacity // 2)
            self.body = self.body[:self.capacity:]

    def return_min(self):
        return min(self.body[:self.size:])


stck = Stack()

n = int(input())
for_print = []

for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))
    if cmd[0] == 1:
        stck.add(cmd[1])
    elif cmd[0] == 2:
        stck.remove_last()
    elif cmd[0] == 3:
        for_print.append(stck.return_min())

sys.stdout.write(('\n'.join(map(str, for_print))))


# 8
# 1 3
# 1 2
# 1 -3
# 2
# 2
# 2
# 1 -3
# 3


# 9
# 1 2
# 1 3
# 1 -3
# 3
# 2
# 3
# 2
# 3
# 2

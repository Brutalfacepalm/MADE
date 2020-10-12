import sys


class Stack:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.body = [None] * self.capacity

    def ensure_capacity(self):
        self.body += [None] * self.capacity
        self.capacity *= 2

    def decline_capacity(self):
        self.capacity = int(self.capacity // 2)
        self.body = self.body[:self.capacity:]

    def push(self, element):
        if self.size >= self.capacity:
            self.ensure_capacity()
        self.body[self.size] = element
        self.size += 1

    def pop(self):
        operand = self.body[self.size - 1]
        self.body[self.size - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 4:
            self.decline_capacity()
        return operand


stack = Stack()

n = sys.stdin.readline().split()

for i in n:
    if i.isdigit():
        stack.push(int(i))
    else:
        if i == '+':
            stack.push(stack.pop() + stack.pop())
        elif i == '-':
            stack.push(- stack.pop() + stack.pop())
        else:
            stack.push(stack.pop() * stack.pop())

print(stack.pop())

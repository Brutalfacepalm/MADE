from itertools import chain
from collections import deque
from sys import stdout, stdin

SEPARATOR = "\n"
UNICODE = "utf-8"


class NodeKey:
    def __init__(self):
        self.A = 5
        self.M = 100
        self.P = 101
        self.N = 20
        self.MIN_CHR = ord('a') - 1
        self.body = deque([[] for _ in range(self.M)])

    def put(self, value):
        hash_key = self.__h(value)
        if self.body[hash_key]:
            if value in self.body[hash_key]:
                return
        self.body[hash_key].append(value)

    def delete(self, value):
        hash_key = self.__h(value)
        if self.body[hash_key] and value in self.body[hash_key]:
            self.body[hash_key].remove(value)

    def get(self, value):
        hash_key = self.__h(value)
        if self.body[hash_key] and value in self.body[hash_key]:
            return True
        return False

    def __h(self, key):
        h = 0
        for i, letter in enumerate(key):
            h += (ord(letter) - self.MIN_CHR) * (self.A ** (self.N - (i + 1)))
        return (h % self.P) % self.M


class MultiMap:
    def __init__(self):
        self.A = 5
        self.M = int(10e4)
        self.P = 2 * int(10e4) + 21
        self.N = 20
        self.MIN_CHR = ord('a') - 1
        self.body = [[] for _ in range(self.M)]

    def put(self, key, value):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            node = self.__check_node(hash_key, key)
            if node:
                check_value = node.get(value)
                if not check_value:
                    node.put(value)
                return
        new_node = NodeKey()
        new_node.put(value)
        self.body[hash_key] += [[key, new_node]]

    def delete(self, key, value):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            node = self.__check_node(hash_key, key)
            if node:
                check_value = node.get(value)
                if check_value:
                    node.delete(value)

    def delete_all(self, key):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            node = self.__check_node(hash_key, key, 'deleteall')
            if node:
                self.body[hash_key].remove(node)

    def get(self, key):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            node = self.__check_node(hash_key, key)
            if node:
                values = list(chain(*[values for values in node.body if values]))
                return f'{len(values)} {" ".join(values)}'
        return '0'

    def __h(self, key):
        h = 0
        for i, letter in enumerate(key):
            h += (ord(letter) - self.MIN_CHR) * (self.A ** (self.N - (i + 1)))
        return (h % self.P) % self.M

    def __check_node(self, hash_key, key, operand='other'):
        index_key = [value for value in self.body[hash_key] if value[0] == key]
        if index_key:
            index_key = index_key[0]
            if operand == 'deleteall':
                return index_key
            else:
                node = index_key[1]
                return node
        else:
            return None


mm = MultiMap()

for cmd in stdin.buffer.read().splitlines():
    cmd = cmd.decode(UNICODE).split()

    if len(cmd) > 0:
        k = cmd[1]
        command = cmd[0]
        if len(cmd) > 2:
            v = cmd[2]
            if command == 'put':
                mm.put(k, v)
            if command == 'delete':
                mm.delete(k, v)
        if command == 'deleteall':
            mm.delete_all(k)
        if command == 'get':
            stdout.buffer.write((mm.get(k) + SEPARATOR).encode(UNICODE))
    else:
        break

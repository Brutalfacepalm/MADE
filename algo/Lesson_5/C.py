from sys import stdin, stdout

SEPARATOR = '\n'
UNICODE = 'utf-8'


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev_node = None
        self.next_node = None


class LinkedMap:
    def __init__(self):
        self.A = 5
        self.M = 50
        self.P = 53
        self.N = 20
        self.MIN_CHR = ord('a') - 1
        self.body = [[] for _ in range(self.M)]
        self.last_put = None

    def put(self, key, value):
        new_node = Node(key, value)
        hash_key = self.__h(key)
        if self.body[hash_key]:
            index_by_hash_key = self.__search_keys(hash_key, key)
            if index_by_hash_key is not None:
                self.body[hash_key][index_by_hash_key].value = value
                return
        self.body[hash_key] += [new_node]
        if self.last_put:
            self.last_put.next_node = new_node
            new_node.prev_node = self.last_put
        self.last_put = new_node

    def delete(self, key):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            index_by_hash_key = self.__search_keys(hash_key, key)
            if index_by_hash_key is not None:
                delete_node = self.body[hash_key].pop(index_by_hash_key)
                if delete_node.prev_node:
                    delete_node.prev_node.next_node = delete_node.next_node
                if delete_node.next_node:
                    delete_node.next_node.prev_node = delete_node.prev_node
                else:
                    self.last_put = delete_node.prev_node

    def get(self, key, operand='current'):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            index_by_hash_key = self.__search_keys(hash_key, key)
            if index_by_hash_key is not None:
                if operand == 'current':
                    return self.body[hash_key][index_by_hash_key].value
                elif operand == 'prev':
                    prev_node = self.body[hash_key][index_by_hash_key].prev_node
                    if prev_node:
                        return prev_node.value
                    else:
                        return 'none'
                elif operand == 'next':
                    next_node = self.body[hash_key][index_by_hash_key].next_node
                    if next_node:
                        return next_node.value
                    else:
                        return 'none'
        return 'none'

    def __h(self, key):
        h = 0
        for i, letter in enumerate(key):
            h += (ord(letter) - self.MIN_CHR) * (self.A ** (self.N - (i + 1)))
        return (h % self.P) % self.M

    def __search_keys(self, hash_key, key):
        ndx = [index for index, key_and_value in enumerate(self.body[hash_key]) if key_and_value.key == key]
        if len(ndx) > 0:
            return ndx[0]
        return None


lm = LinkedMap()

for cmd in stdin.buffer.read().splitlines():
    cmd = cmd.decode(UNICODE).split()
    if len(cmd) > 0:
        k = cmd[1]
        command = cmd[0]
        if len(cmd) > 2:
            v = cmd[2]
            if command == 'put':
                lm.put(k, v)
        if command == 'delete':
            lm.delete(k)
        if command == 'get':
            stdout.buffer.write((lm.get(k) + SEPARATOR).encode(UNICODE))
        if command == 'prev':
            stdout.buffer.write((lm.get(k, 'prev') + SEPARATOR).encode(UNICODE))
        if command == 'next':
            stdout.buffer.write((lm.get(k, 'next') + SEPARATOR).encode(UNICODE))
    else:
        break

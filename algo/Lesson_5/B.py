from sys import stdin, stdout

SEPARATOR = '\n'
UNICODE = 'utf-8'


class MapChain:
    def __init__(self):
        self.A = 5
        self.M = 5000
        self.P = 7717
        self.N = 20
        self.MIN_CHR = ord('a') - 1
        self.body = [[] for _ in range(self.M)]

    def put(self, key, value):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            index_by_hash_key = self.__search_keys(hash_key, key)
            if index_by_hash_key is not None:
                self.body[hash_key][index_by_hash_key][1] = value
                return
        self.body[hash_key] = self.body[hash_key] + [[key, value]]

    def delete(self, key):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            index_by_hash_key = self.__search_keys(hash_key, key)
            if index_by_hash_key is not None:
                self.body[hash_key].pop(index_by_hash_key)

    def get(self, key):
        hash_key = self.__h(key)
        if self.body[hash_key]:
            index_by_hash_key = self.__search_keys(hash_key, key)
            if index_by_hash_key is not None:
                return self.body[hash_key][index_by_hash_key][1]
        return 'none'

    def __h(self, key):
        h = 0
        for i, letter in enumerate(key):
            h += (ord(letter) - self.MIN_CHR) * (self.A ** (self.N - (i + 1)))
        return (h % self.P) % self.M

    def __search_keys(self, hash_key, key):
        index_by_hash_key = [index for index, key_and_value in enumerate(self.body[hash_key]) if key_and_value[0] == key]
        if len(index_by_hash_key) > 0:
            return index_by_hash_key[0]
        return None


mc = MapChain()

for cmd in stdin.buffer.read().splitlines():
    cmd = cmd.decode(UNICODE).split()

    if len(cmd) > 0:
        k = cmd[1]
        command = cmd[0]
        if len(cmd) > 2:
            v = cmd[2]
            if command == 'put':
                mc.put(k, v)
        if command == 'delete':
            mc.delete(k)
        if command == 'get':
            stdout.buffer.write((mc.get(k) + SEPARATOR).encode(UNICODE))
    else:
        break

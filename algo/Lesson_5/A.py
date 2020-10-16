from sys import stdin, stdout

SEPARATOR = '\n'
UNICODE = 'utf-8'


class SetOpenHash:
    def __init__(self):
        self.M = 2 * int(10e5)
        self.body = [None] * self.M

    def insert(self, new_element):
        i_for_new_element = self.__h(new_element)
        for _ in self.body:
            if self.body[i_for_new_element] is None:
                self.body[i_for_new_element] = new_element
                break
            elif self.body[i_for_new_element] == new_element:
                break
            else:
                i_for_new_element = (i_for_new_element + 1) % self.M

    def delete(self, element_for_delete):
        i_for_delete_element = self.__h(element_for_delete)
        j = i_for_delete_element
        for _ in self.body:
            if self.body[j] is None:
                break
            elif self.body[j] == element_for_delete:
                self.body[j] = None

                if j != i_for_delete_element:
                    s = j + 1
                    while s < self.M and self.body[s] is not None:
                        if j == self.__h(self.body[s]):
                            self.body[s], self.body[j] = self.body[j], self.body[s]
                        j = s
                        s += 1
                break
            else:
                j = (j + 1) % self.M

    def exists(self, element_for_exist):
        i_for_exist_element = self.__h(element_for_exist)

        if self.body[i_for_exist_element] is None:
            return 'false'
        elif self.body[i_for_exist_element] == element_for_exist:
            return 'true'
        else:
            return 'false'

    def __h(self, x):
        return x % self.M


soh = SetOpenHash()

for cmd in stdin.buffer.read().splitlines():
    cmd = cmd.decode(UNICODE).split()

    if len(cmd) > 0:
        element = int(cmd[1])
        cmd = cmd[0]
        if cmd == 'insert':
            soh.insert(element)
        if cmd == 'delete':
            soh.delete(element)
        if cmd == 'exists':
            stdout.buffer.write((soh.exists(element) + SEPARATOR).encode(UNICODE))
    else:
        break

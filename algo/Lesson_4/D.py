import sys
import math


class Node:
    def __init__(self, data):
        self.data = data
        self.i_push = None
        self.position = None


class Heap:
    def __init__(self):
        self.size = 0
        self.body = []
        self.commands = 1
        self.push_in_commands = []

    def push(self, new_element):
        self.body.append(new_element)
        new_element.i_push = self.commands
        self.push_in_commands.append(new_element)

        self.__sift_up(self.size, self.body[self.size])

        self.commands += 1
        self.size += 1

    def extract_min(self):
        self.commands += 1
        self.push_in_commands.append(None)
        if self.body:
            self.body[0], self.body[-1] = self.body[-1], self.body[0]
            is_min = self.body.pop()
            self.size -= 1
            if self.size > 1:
                self.body[0].position = 0
                self.__sift_down()
            self.push_in_commands[is_min.i_push - 1] = None
        else:
            return '*'
        return ' '.join(list(map(str, [is_min.data, is_min.i_push])))

    def decrease(self, node_position, new_value):
        self.commands += 1
        self.push_in_commands.append(None)
        decrease_node = self.push_in_commands[node_position - 1]
        if decrease_node:
            if decrease_node.data > new_value:
                decrease_node.data = new_value
                if len(self.body) > 1:
                    self.__sift_up(decrease_node.position, decrease_node)

    def __sift_up(self, current_i, sift_node):
        while current_i > 0:
            desc_i = math.floor((current_i - 1) / 2)

            if self.body[desc_i].data > sift_node.data:
                self.body[desc_i].position = current_i
                self.body[desc_i], self.body[current_i] = self.body[current_i], self.body[desc_i]
                current_i = desc_i
            else:
                break

        self.body[current_i].position = current_i

    def __sift_down(self):
        sift_node = self.body[0]
        current_i = 0
        while current_i < self.size:
            desc_i_left = 2 * current_i + 1
            desc_i_right = 2 * current_i + 2
            if self.size > desc_i_right and self.body[desc_i_left].data > self.body[desc_i_right].data:
                desc_i = desc_i_right
            elif self.size > desc_i_left:
                desc_i = desc_i_left
            else:
                break
            if self.body[desc_i].data < sift_node.data:
                self.body[desc_i].position = current_i
                self.body[current_i].position = desc_i
                self.body[desc_i], self.body[current_i] = self.body[current_i], self.body[desc_i]
                current_i = desc_i
            else:
                break


heap = Heap()

for cmd in sys.stdin:
    cmd = cmd.split()
    if len(cmd) > 0:
        if cmd[0] == 'push':
            heap.push(Node(int(cmd[1])))
        if cmd[0] == 'decrease-key':
            heap.decrease(int(cmd[1]), int(cmd[2]))
        if cmd[0] == 'extract-min':
            print(heap.extract_min())
    else:
        break

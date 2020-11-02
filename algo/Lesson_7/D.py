from sys import stdin, stdout
import math

SEPARATOR = "\n"
UNICODE = "utf-8"


class Node:
    def __init__(self, i, ai, include, is_leaf=True):
        self.index = i
        self.value = ai
        self.include = include
        self.is_leaf = is_leaf
        self.root = False
        self.left_child = None
        self.right_child = None
        self.parent = False

    def set_upd(self, u):
        self.upd = u

    def set_root(self):
        self.root = True


class CutTree:

    def _get_body(self, n, a):
        self.body = [Node(i, math.inf, []) for i in range(2 * 2 ** int(math.ceil(math.log2(n))) - 1)]
        x = 2 ** int(math.ceil(math.log2(n)))

        for i in range(n):
            self.body[i + x - 1] = Node(i, a[i], [i])

        if n > 1:
            for v in range(x - 2, -1, -1):
                left_child = self.body[2 * v + 1]
                right_child = self.body[2 * v + 2]
                min_value = min(left_child.value, right_child.value)
                if left_child.include and right_child.include:
                    include = [left_child.include[0], right_child.include[-1]]
                elif left_child.include and not right_child.include:
                    include = [left_child.include[0], left_child.include[-1]]
                else:
                    include = []

                self.body[v] = Node(v, min_value, include, False)
                if v == 0:
                    self.body[v].set_root()
                left_child.parent = self.body[v]
                right_child.parent = self.body[v]
                self.body[v].left_child = left_child
                self.body[v].right_child = right_child

    def push_down(self, node, x):
        if not node.is_leaf:
            node.left_child.value += node.upd
            node.right_child.value += node.upd
            node.left_child.set_upd(x)
            node.right_child.set_upd(x)
            self.push_down(node.left_child, x)
            self.push_down(node.right_child, x)
        else:
            return
        node.set_upd(0)

    def push_down_set(self, node, x):
        if not node.is_leaf:
            node.left_child.value = x
            node.right_child.value = x
            self.push_down_set(node.left_child, x)
            self.push_down_set(node.right_child, x)
        else:
            return

    def push_up(self, node):
        if node.root:
            return
        else:
            node.parent.value = min(node.parent.left_child.value, node.parent.right_child.value)
            self.push_up(node.parent)

    def set(self, node, l, r, a, b, x):
        if l > b or r < a:
            return
        if l >= a and r <= b:
            node.value = x
            if n > 1:
                self.push_down_set(node, x)
                self.push_up(node)
            return

        left_node = self.body[2 * node.index + 1]
        right_node = self.body[2 * node.index + 2]

        self.set(left_node, left_node.include[0], left_node.include[-1], a, b, x)
        self.set(right_node, right_node.include[0], right_node.include[-1], a, b, x)

    def add(self, node, l, r, a, b, x):
        if l > b or r < a:
            return
        if l >= a and r <= b:
            node.value += x
            node.set_upd(x)
            if n > 1:
                self.push_down(node, x)
                self.push_up(node)
            return

        left_node = self.body[2 * node.index + 1]
        right_node = self.body[2 * node.index + 2]
        self.add(left_node, left_node.include[0], left_node.include[-1], a, b, x)
        self.add(right_node, right_node.include[0], right_node.include[-1], a, b, x)

    def search_min(self, node, l, r, a, b):
        if l > b or r < a:
            return math.inf
        if l >= a and r <= b:
            return node.value

        left_node = self.body[2 * node.index + 1]
        right_node = self.body[2 * node.index + 2]
        return min(self.search_min(left_node, left_node.include[0], left_node.include[-1], a, b),
                   self.search_min(right_node, right_node.include[0], right_node.include[-1], a, b))


rmq = CutTree()

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
        rmq._get_body(n, a)

    else:
        i = int(cmd[1])
        j = int(cmd[2])
        if j > n:
            j = n
        if i > n:
            i = n
            j = i
        if len(cmd) > 3:
            x = int(cmd[3])
        command = cmd[0]
        node = rmq.body[0]
        l = node.include[0]
        r = node.include[-1]
        if command == 'add':
            rmq.add(node, l, r, i - 1, j - 1, x)
        if command == 'set':
            rmq.set(node, l, r, i - 1, j - 1, x)
        if command == 'min':
            r = rmq.search_min(node, l, r, i - 1, j - 1)
            stdout.buffer.write((str(r) + SEPARATOR).encode(UNICODE))

# 1
# 1
# add 1 1 -10
# min 1 1
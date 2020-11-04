from sys import stdin, stdout

SEPARATOR = '\n'
UNICODE = 'utf-8'


class EmptyNode:
    def __init__(self):
        self.value = None
        self.h = 0

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = EmptyNode()
        self.right_child = EmptyNode()
        self.is_root = False
        self.h = 1
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, node_parent, x):
        if not node or node.value is None:
            if self.root is None:
                self.root = Node(x)
                self.root.is_root = True
                return root
            n = Node(x)
            n.parent = node_parent
            self.update_h(n, 1)
            return n
        elif node.value > x:
            node.left_child = self.insert(node.left_child, node, x)
        elif node.value < x:
            node.right_child = self.insert(node.right_child, node, x)
        return node

    def update_h(self, node, delta):
        while node.parent.value is not None:
            node.parent.h += delta
            node = node.parent
            if node.parent is None:
                break

    def balanced(self, node):
        if node.right_child.h - node.left_child.h == 2:
            if
            self.rotate_left(node)
        if node.right_child.h - node.left_child.h == -2:
            self.rotate_right(node)

    def delete(self, node, x):
        if not node:
            return None
        elif node.value > x:
            node.left_child = self.delete(node.left_child, x)
        elif node.value < x:
            node.right_child = self.delete(node.right_child, x)
        else:
            if node.right_child is None and node.left_child is None:
                if node.is_root:
                    self.root = None
                node = None
            elif node.left_child is None:
                if node.is_root:
                    node.right_child.is_root = True
                    self.root = node.right_child
                node = node.right_child
            elif node.right_child is None:
                if node.is_root:
                    node.left_child.is_root = True
                    self.root = node.left_child
                node = node.left_child
            else:
                node.value = self._find_max(node.left_child).value
                node.left_child = self.delete(node.left_child, node.value)
        return node

    def exists(self, node, x):
        if not node:
            return 'false'
        elif node.value > x:
            return self.exists(node.left_child, x)
        elif node.value < x:
            return self.exists(node.right_child, x)
        return 'true'

    def get_next_or_prev(self, node, x, next_or_prev, res='none'):
        while node:
            if next_or_prev == 'next':
                if node.value > x:
                    res = str(node.value)
                    node = node.left_child
                else:
                    node = node.right_child
            else:
                if node.value < x:
                    res = str(node.value)
                    node = node.right_child
                else:
                    node = node.left_child
        return res

    def _find_max(self, node):
        while node.right_child:
            node = node.right_child
        return node

    def _find_min(self, node):
        while node.left_child:
            node = node.left_child
        return node

    def print_tree(self, node, s=''):
        if node:
            s += '__'
            self.print_tree(node.left_child, s)
            print(s, node.value)
            self.print_tree(node.right_child, s)


bst = BinarySearchTree()

for cmd in stdin.buffer:
    cmd = cmd.strip().decode(UNICODE).split()

    if cmd:
        command = cmd[0]
        x = int(cmd[1])
        root = bst.root

        if command == 'insert':
            bst.insert(root, EmptyNode(), x)
        if command == 'delete':
            bst.delete(root, x)
        if command == 'exists':
            stdout.buffer.write((bst.exists(root, x) + SEPARATOR).encode(UNICODE))
        if command == 'next':
            stdout.buffer.write((bst.get_next_or_prev(root, x, 'next') + SEPARATOR).encode(UNICODE))
        if command == 'prev':
            stdout.buffer.write((bst.get_next_or_prev(root, x, 'prev') + SEPARATOR).encode(UNICODE))
    else:
        break

print(bst.root.h)
print(bst.root.right_child.h)
print(bst.root.right_child.left_child.h)
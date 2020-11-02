from sys import stdin, stdout

SEPARATOR = '\n'
UNICODE = 'utf-8'


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.is_root = False

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, x):
        if not node:
            if self.root is None:
                self.root = Node(x)
                self.root.is_root = True
                return root
            return Node(x)
        elif node.value > x:
            node.left_child = self.insert(node.left_child, x)
        elif node.value < x:
            node.right_child = self.insert(node.right_child, x)
        return node

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
                    # print(node.value)
                    res = str(node.value)
                    node = node.left_child
                    # print('left')
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


    # def _get_next_and_up(self, node):
    #     while node.left_child:
    #         node = node.left_child
    #     value = node.value
    #     node = None
    #     return value
    #
    # def _get_prev_and_up(self, node):
    #     while node.right_child:
    #         node = node.right_child
    #     value = node.value
    #     node = None
    #     return value


bst = BinarySearchTree()

for cmd in stdin.buffer:
    cmd = cmd.strip().decode(UNICODE).split()
# for _ in range(100):
#     cmd = input().split()
    if cmd:
        command = cmd[0]
        x = int(cmd[1])
        root = bst.root
        # try:
        #     print('root', root.value)
        # except:
        #     pass
        # print('TREE')
        # bst.print_tree(root)
        # print('')

        if command == 'insert':
            bst.insert(root, x)
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


# insert 3
# insert 3
# delete 3
# exists 3
# next 2
# prev 4



# insert 2
# insert 5
# insert 6
# insert 3
# exists 2
# exists 4
# next 4
# prev 4
# delete 5
# exists 5
# delete 6
# exists 3
# delete 3
# delete 2
# exists 2
# insert 1
# insert 7
# insert 6
# insert 9
# insert 2
# insert 3
# exists 4
# next 4
# prev 4

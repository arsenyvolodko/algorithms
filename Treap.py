import random


class Node:
    def __init__(self, key):
        self.key = key
        self.size = 1
        self.priority = random.randint(-10 ** 9, 10 ** 9)
        self.right = None
        self.left = None

    def update(self):
        self.size = (0 if not self.left else self.left.size) + (
            0 if not self.right else self.right.size) + 1


class Treap:

    def __init__(self, array=None):
        self.root = None
        for i in array:
            self.insert(i)

    def size(self):
        return 0 if not self.root else self.root.size

    def merge(self, node1: Node, node2: Node):
        if not node2:
            return node1
        if not node1:
            return node2
        elif node1.priority > node2.priority:
            node1.right = self.merge(node1.right, node2)
            if node1:
                node1.update()
            return node1
        else:
            node2.left = self.merge(node1, node2.left)
            if node2:
                node2.update()
            return node2

    def split(self, node: Node, k):
        if node is None:
            return None, None

        elif node.key < k:
            node.right, t2 = self.split(node.right, k)
            if t2:
                t2.update()
            if node:
                node.update()
            return node, t2
        else:
            t1, node.left = self.split(node.left, k)
            if t1:
                t1.update()
            if node:
                node.update()
            return t1, node

    def insert(self, key):
        less, greater = self.split(self.root, key)
        equal, greater = self.split(greater, key + 1)
        if not equal:
            self.root = self.merge(self.merge(less, Node(key)), greater)
        else:
            self.root = self.merge(self.merge(less, equal), greater)

    def contains(self, key):
        (less, greater) = self.split(self.root, key)
        (equal, greater) = self.split(greater, key + 1)
        self.root = self.merge(self.merge(less, equal), greater)
        return equal is not None

    def remove(self, key):
        (less, greater) = self.split(self.root, key)
        (equal, greater) = self.split(greater, key + 1)
        self.root = self.merge(less, greater)

    def prev_key(self, key1, key2):
        (less, greater) = self.split(self.root, key1)
        (middle, greater) = self.split(greater, key2)
        self.root = self.merge(self.merge(less, middle), greater)
        if middle:
            return middle.size

    def index_by_key(self, key):
        (less, greater) = self.split(self.root, key)
        res = 0 if not less else less.size
        self.root = self.merge(less, greater)
        return res

    def key_by_index(self, index):
        return self.__key_by_index_in(self.root, index)

    def __key_by_index_in(self, node, index):
        l_size = 0 if not node.left else node.left.size
        if index == l_size:
            return node.key
        if index < l_size:
            return self.__key_by_index_in(node.left, index)
        else:
            return self.__key_by_index_in(node.right, index - l_size - 1)

    def prev(self, K, def_val=None):
        q = self.__prev_in(self.root, None, K)
        if q is not None:
            return q.key
        else:
            return def_val

    def __prev_in(self, node, prev_node, K):
        if node is not None:
            if node.key == K:
                return node
            elif node.key < K:
                prev_node = node
                node = node.right
                return self.__prev_in(node, prev_node, K)
            else:
                node = node.left
                return self.__prev_in(node, prev_node, K)
        return prev_node

    def next(self, K, def_val=None):
        q = self.__next_in(self.root, None, K)
        if q is not None:
            return q.key
        else:
            return def_val

    def __next_in(self, node, next_node, K):
        if node is not None:
            if node.key == K:
                if node.right is not None:
                    return self.__find_min(node.right)
                else:
                    return next_node
            elif node.key > K:
                next_node = node
                node = node.left
                return self.__next_in(node, next_node, K)
            else:
                node = node.right
                return self.__next_in(node, next_node, K)
        return next_node

    @staticmethod
    def __find_min(node):
        while node.left is not None:
            node = node.left
        return node

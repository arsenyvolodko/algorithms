class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self, array: list = None):
        self.__cnt = 0
        self.__root = None
        if array is not None:
            for i in array:
                self.insert(i)

    def size(self):
        return self.__cnt

    def insert(self, x: int):
        self.__root = self.__insert_util(self.__root, x)
        self.__cnt += 1

    def __insert_util(self, node, x):
        if node is None:
            return Node(x)
        elif x < node.val:
            node.left = self.__insert_util(node.left, x)
        else:
            node.right = self.__insert_util(node.right, x)

        node.height = max(self.__get_height(node.right), self.__get_height(node.left)) + 1

        balance = self.__get_balance(node)

        if -1 > balance and node.right.val < x:
            return self.__left_rotate(node)

        if 1 < balance and node.left.val > x:
            return self.__right_rotate(node)

        if -1 > balance and node.right.val > x:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        if 1 < balance and node.left.val < x:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        return node

    def remove(self, key: int):
        if self.contains(key):
            self.__root = self.__remove_util(self.__root, key)
            self.__cnt -= 1

    def __remove_util(self, node, key):
        if node is None:
            return node
        elif node.val > key:
            node.left = self.__remove_util(node.left, key)
        elif node.val < key:
            node.right = self.__remove_util(node.right, key)

        else:
            if node.left is None:
                temp = node.right
                return temp

            elif node.right is None:
                temp = node.left
                return temp

            temp = self.__get_min_node(node.right)
            node.val = temp.val
            node.right = self.__remove_util(node.right, temp.val)

        if node is None:
            return node

        node.height = max(self.__get_height(node.right), self.__get_height(node.left)) + 1

        balance = self.__get_balance(node)

        if -1 > balance and self.__get_balance(node.right) <= 0:
            return self.__left_rotate(node)

        if 1 < balance and self.__get_balance(node.left) >= 0:
            return self.__right_rotate(node)

        if -1 > balance and self.__get_balance(node.right) > 0:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        if 1 < balance and self.__get_balance(node.left) < 0:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        return node

    def max(self):
        return self.__get_max_node(self.__root).val

    def __get_max_node(self, node):
        if node is None or node.right is None:
            return node

        return self.__get_max_node(node.right)

    def min(self):
        return self.__get_min_node(self.__root).val

    def __get_min_node(self, node):
        if node is None or node.left is None:
            return node

        return self.__get_min_node(node.left)

    def __left_rotate(self, node):
        new_node = node.right
        p = new_node.left
        new_node.left = node
        node.right = p

        node.height = max(self.__get_height(node.right), self.__get_height(node.left)) + 1
        new_node.height = max(self.__get_height(new_node.right), self.__get_height(new_node.left)) + 1
        return new_node

    def __right_rotate(self, node):
        new_node = node.left
        p = new_node.right
        new_node.right = node
        node.left = p

        node.height = max(self.__get_height(node.right), self.__get_height(node.left)) + 1
        new_node.height = max(self.__get_height(new_node.right), self.__get_height(new_node.left)) + 1
        return new_node

    def __get_height(self, node):
        if node is None:
            return 0
        return node.height

    def __get_balance(self, node):
        if node is None:
            return 0
        return self.__get_height(node.left) - self.__get_height(node.right)

    def contains(self, key: int):
        q = self.__contains_util(self.__root, key)
        if q is None:
            return False
        else:
            return True

    def __contains_util(self, node, key):

        if node is None or node.val == key:
            return node

        if node.val < key:
            return self.__contains_util(node.right, key)

        else:
            return self.__contains_util(node.left, key)

    def next(self, key: int):
        if self.__cnt == 0:
            return None
        q = self.__next_in(self.__root, None, key)
        if q is not None:
            return q.val
        else:
            return None

    def __next_in(self, node, suc_node, key):
        while node is not None:
            if node.val == key:
                if node.right:
                    suc_node = node.right
                    while suc_node.left:
                        suc_node = suc_node.left
                return suc_node
            elif node.val < key:
                node = node.right
            else:
                suc_node = node
                node = node.left
        return suc_node

    def prev(self, key: int):
        if self.__cnt == 0:
            return None
        q = self.__prev_in(self.__root, None, key)
        if q is not None:
            return q.val
        else:
            return None

    def __prev_in(self, node, prev_node, key):
        while node is not None:
            if node.val == key:
                if node.left:
                    prev_node = node.left
                    while prev_node.right:
                        prev_node = prev_node.right
                return prev_node
            elif node.val < key:
                prev_node = node
                node = node.right
            else:
                node = node.left
        return prev_node

class SumSegmentTree:
    def __init__(self, array: list):
        self.tree = [0] * len(array) * 4
        self.array = array.copy()
        self.n = len(array)
        self.__build(1, 0, self.n - 1)

    def __build(self, cur_ind, cur_l, cur_r):
        if cur_l == cur_r:
            self.tree[cur_ind] = self.array[cur_l]
        else:
            m = (cur_l + cur_r) // 2
            self.__build(2 * cur_ind, cur_l, m)
            self.__build(2 * cur_ind + 1, m + 1, cur_r)
            self.tree[cur_ind] = self.tree[2 * cur_ind] + self.tree[2 * cur_ind + 1]

    def sum(self, l: int, r: int):
        return self.__get_sum_util(l, r - 1, 1, 0, self.n - 1)

    def __get_sum_util(self, l, r, cur_ind, cur_l, cur_r):
        if l <= cur_l and cur_r <= r:
            return self.tree[cur_ind]

        if cur_r < l or r < cur_l:
            return 0

        m = (cur_l + cur_r) // 2
        return self.__get_sum_util(l, r, cur_ind * 2, cur_l, m) + \
               self.__get_sum_util(l, r, cur_ind * 2 + 1, m + 1, cur_r)

    def set(self, ind: int, new_val: int):
        self.__set_util(ind, new_val, 1, 0, self.n - 1)

    def __set_util(self, ind, new_val, cur_ind, cur_l, cur_r):
        if cur_l >= ind >= cur_r:
            self.array[ind] = new_val
            self.tree[cur_ind] = new_val
            return

        if cur_r < ind or ind < cur_l:
            return

        m = (cur_l + cur_r) // 2
        self.__set_util(ind, new_val, cur_ind * 2, cur_l, m)
        self.__set_util(ind, new_val, cur_ind * 2 + 1, m + 1, cur_r)
        self.tree[cur_ind] = self.tree[cur_ind * 2] + self.tree[cur_ind * 2 + 1]

    def get(self, ind: int):
        return self.array[ind]

    def get_all(self):
        return self.array

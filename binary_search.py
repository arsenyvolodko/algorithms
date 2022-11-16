# returns index of the first occurrence of the element x in sorted array if it's exists
# or index where it will be placed if element is missed
def leftmost_bin_search(array: list, x: int):
    l = 0
    r = len(array)
    while l < r:
        m = (l + r) // 2
        if array[m] < x:
            l = m + 1
        else:
            r = m
    return r if r != -1 else 0


# returns index of the last occurrence of the element x in sorted array if it's exists
# or index where it will be placed if element is missed
def rightmost_bin_search(array: list, x: int):
    l = 0
    r = len(array)
    while l < r:
        m = (l + r) // 2
        if array[m] > x:
            r = m
        else:
            l = m + 1
    return r - 1


# returns index of the first occurrence of the element x in sorted array if it's exists, else -1
def contains(array: list, x: int):
    x_ind = leftmost_bin_search(array, x)
    if not (0 <= x_ind < len(array)) or array[x_ind] != x:
        return -1
    return x_ind


# returns number of occurrences of the element x in sorted array
def count(array: list, x: int):
    return len(array) - greater_than_x(array, x) - less_than_x(array, x)


# returns number of elements less than x in sorted array
def less_than_x(array: list, x: int):
    l = leftmost_bin_search(array, x)
    return l


# returns number of elements less than or equal to x in sorted array
def less_or_equals_x(array: list, x: int):
    return len(array) - greater_than_x(array, x)


# returns number of elements greater than or equal to x in sorted array
def greater_than_x(array: list, x: int):
    if x > array[-1]:
        return 0
    if x < array[0]:
        return len(array)
    r = rightmost_bin_search(array, x)
    return len(array) - r - 1


# returns number of elements greater than or equal to x in sorted array
def greater_or_equals_x(array: list, x: int):
    return len(array) - less_than_x(array, x)

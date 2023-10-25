# basic binary search
def binary_search(array: list[int], x: int):
    left = 0
    right = len(array)
    while left < right:
        m = (left + right) // 2
        if array[m] < x:
            left = m + 1
        else:
            right = m
    if (0 <= right < len(array)) and array[right] == x:
        return right
    return -1


# returns index of the first occurrence of the element x in sorted array if it's exists
# or index where it will be placed if element is missed
def leftmost_bin_search(array: list[int], x: int):
    left = 0
    right = len(array)
    while left < right:
        m = (left + right) // 2
        if array[m] < x:
            left = m + 1
        else:
            right = m
    return right if right != -1 else 0


# returns index of the last occurrence of the element x in sorted array if it's exists
# or index where it will be placed if element is missed
def rightmost_bin_search(array: list[int], x: int):
    left = 0
    right = len(array)
    while left < right:
        m = (left + right) // 2
        if array[m] > x:
            right = m
        else:
            left = m + 1
    return right - 1


# returns index of the first occurrence of the element x in sorted array if it's exists, else -1
def contains(array: list[int], x: int):
    x_ind = leftmost_bin_search(array, x)
    if not (0 <= x_ind < len(array)) or array[x_ind] != x:
        return -1
    return x_ind


# returns number of occurrences of the element x in sorted array
def count(array: list[int], x: int):
    return len(array) - greater_than_x(array, x) - less_than_x(array, x)


# returns number of elements less than x in sorted array
def less_than_x(array: list[int], x: int):
    left = leftmost_bin_search(array, x)
    return left


# returns number of elements less than or equal to x in sorted array
def less_or_equals_x(array: list[int], x: int):
    return len(array) - greater_than_x(array, x)


# returns number of elements greater than or equal to x in sorted array
def greater_than_x(array: list[int], x: int):
    if x > array[-1]:
        return 0
    if x < array[0]:
        return len(array)
    right = rightmost_bin_search(array, x)
    return len(array) - right - 1


# returns number of elements greater than or equal to x in sorted array
def greater_or_equals_x(array: list[int], x: int):
    return len(array) - less_than_x(array, x)

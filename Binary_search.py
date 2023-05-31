def binary_search(list, target, low, high):
    if low > high:
        return -1
    mid = int((low + high) / 2)
    mid_value = list[mid]
    if mid_value == target:
        return mid
    elif mid_value < target:
        return binary_search(list, target, mid + 1, high)
    else:
        return binary_search(list, target, low, mid - 1)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(list, 5, 0, 8))

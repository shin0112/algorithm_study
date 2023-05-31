def Merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def Merge_Sort(list):
    if len(list) < 2:
        return list

    mid = len(list) // 2
    left = Merge_Sort(list[:mid])
    right = Merge_Sort(list[mid:])
    return Merge(left, right)


list = [3, 1, 6, 7, 4, 23, 17, 14, 30, 41, 26, 12]
print(Merge_Sort(list))

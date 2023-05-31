import sys
sys.setrecursionlimit(10000)


def Median_of_Medians(arr):
    if len(arr) <= 5:
        return findMedian(arr)
    medians = []
    for i in range(int(len(arr) / 5)):
        group = arr[i * 5: min((i + 1) * 5, len(arr))]
        median = findMedian(group)
        medians.append(median)
    approximate_median = Median_of_Medians(medians)
    return approximate_median


def findMedian(arr):
    arr.sort()
    return arr[len(arr) // 2]


def Quick_Sort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)
        Quick_Sort(arr, low, pivotIndex - 1)
        Quick_Sort(arr, pivotIndex + 1, high)


def partition(arr, low, high):
    pivot = Median_of_Medians(arr)
    for i in range(low, high + 1):
        if arr[i] == pivot:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    i = low - 1
    for j in range(low, high):
        if arr[i] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[low] = arr[low], arr[i + 1]
#    arr.sort()
    return i + 1


list = [1, 7, 4, 5, 9, 8, 6, 3, 2, 11, 24, 42, 12, 39]
# [1, 7, 4, 5, 9]   5
# [8, 6, 3, 2, 11]  6       6
# [24, 42, 12, 39]  24
print(Median_of_Medians(list))
Quick_Sort(list, 0, 8)
print(list)

# Radix Sort(기수정렬)
# 가장 낮은 자리의 수를 기준으로 정렬하고 가장 높은 자리의 수까지 다음 자리 수르 기준으로 이 과정을 반복하여 정렬하는 알고리즘

def radixSort(arr):
    maxVal = max(arr)
    count = 1

    while maxVal > count:
        buckets = [[] for _ in range(10)]
        for j in arr:
            digit = (j // count) % 10
            buckets[digit].append(j)

        arr = []
        for bucket in buckets:
            for num in bucket:
                arr.append(num)
        count *= 10

    return arr


arr = [20, 91, 35, 7, 65, 69, 85, 73, 46, 120, 243]
print(radixSort(arr))

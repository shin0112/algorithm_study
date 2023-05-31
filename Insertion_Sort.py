def Insertion_Sort(a):
    for j in range(1, len(a)):
        for i in range(j, 0, -1):
            if a[i - 1] > a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
    return a


# s_string = input().split()
# sort_list_example = list(map(int, s_string))
sort_list_example = [10, 7, 11, 5, 13, 8]
print(Insertion_Sort(sort_list_example), end="\n\n")  # [5, 7, 8, 10, 11, 13]

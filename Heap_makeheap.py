import math


class heap(object):
    n = 0

    def __init__(self, data):
        self.data = data
        self.n = len(self.data) - 1

    def addElt(self, elt):
        self.data.append(elt)
        self.n += 1

    def siftUp(self, i):
        while i >= 2:
            i = 0

    def siftDown(self, i):
        key = self.data[i]
        parent = i
        spot_found = False

        while 2 * parent <= self.n and not(spot_found):
            if 2 * parent < self.n and self.data[2 * parent] < self.data[2 * parent + 1]:
                larger_child = 2 * parent + 1
            else:
                larger_child = 2 * parent
            if key < self.data[larger_child]:
                self.data[parent] = self.data[larger_child]
                parent = larger_child
            else:
                spot_found = True

        self.data[parent] = key

    def makeHeap2(self):
        for i in range(int(self.n / 2), 1, -1):
            self.siftDown(i)

    def root(self):
        out = self.data[1]
        self.data[1] = self.data[self.n]
        self.n -= 1
        self.siftDown(1)
        return out

# 인덱스 단순화를 위해 0 처음 element 0 추가
a = [0, 11, 14, 2, 7, 6, 3, 9, 5]
b = heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
# s = heapSort(a)
# print(s)

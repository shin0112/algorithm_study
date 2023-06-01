import math
class heap(object):
    n = 0

# data(heap list로 표현), n(element 개수)
    def __init__(self, data):
        self.data = data
        self.n = len(self.data) - 1

# element 추가
    def addElt(self, elt):
        self.data.append(elt)
        self.n += 1
        self.siftUp(self.n)

# 마지막 element 들어올 때마다 heap 재구성
    def siftUp(self, i):
        while i >= 2:
            if self.data[i] > self.data[i // 2]:
                self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
                i = i // 2
            else:
                return


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
    
    def makeHeap1(self):
        for i in range(self.n):
            self.siftUp(i)

    def makeHeap2(self):
        for i in range(self.n // 2, 0, -1):
            self.siftDown(i)

    def root(self):
        if self.n == 0:
            return
        out = self.data[1]
        self.data[1] = self.data[self.n]
        self.n -= 1
        self.siftDown(1)
        return out
    
    def removeKeys(self):
        a = []
        for i in range(self.n):
            a.append(self.root())
        return a


def heapSort(a):
    h = heap(a)
    return h.removeKeys()

# 인덱스 단순화를 위해 0 처음 element 0 추가
print("방법 1을 이용하여 makeHeap 구현")
a = [0, 17, 14, 2, 7, 6, 3, 9, 5]
b = heap(a)
b.makeHeap1()
print(b.data)
s = heapSort(a)
print(s)


print("\n방법 2를 이용하여 makeHeap 구현")
a = [0, 11, 14, 2, 7, 8, 3, 10, 5]
b = heap(a)
b.makeHeap2()
print(b.data)
b.addElt(30)
print(b.data)
s = heapSort(a)
print(s)


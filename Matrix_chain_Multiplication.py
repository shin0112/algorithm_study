import numpy as np
# [문제] 연쇄행렬 최소 곱셈 알고리즘 프로그램 완성 및 order(1,5) 출력

def printMatrix(d):
    n = len(d[0])
    for i in range(1, n):
        for j in range(1, n):
            print("{0: < 5}".format(d[i][j]), end="  ")
        print()
    print()


def min_mul(n, d, P):
    M = [[0 for i in range(n)] for j in range(n)]
    for diagonal in range(1, n):
        for i in range(1, n - diagonal):
            j = i + diagonal
            for k in range(i, j):
                if M[i][j] == 0:
                    M[i][j] = M[i][k] + M[k + 1][j] + d[i-1]*d[k]*d[j]
                    P[i][j] = k
    print("행렬 M 출력")
    printMatrix(M)
    return M[1][n - 1]


def order(i, j):
    if i == j:
        print("A{}".format(i), end="")
    else:
        k = P[i][j]
        print("(", end="")
        order(i, k)
        order(k + 1, j)
        print(")", end="")


data1 = (np.random.randn(4, 4) * 10).astype(np.int32)
data2 = (np.random.randn(4, 3) * 10).astype(np.int32)
data3 = (np.random.randn(3, 5) * 10).astype(np.int32)
data4 = (np.random.randn(5, 3) * 10).astype(np.int32)
data5 = (np.random.randn(3, 2) * 10).astype(np.int32)
d = [4, 4, 3, 5, 3, 2]
n = len(d)
P = [[0 for j in range(1, n + 1)] for i in range(1, n + 1)]
print("[문제] 연쇄행렬 최소 곱셈 알고리즘 프로그램 완성 및 order(1,5) 출력")
result = min_mul(n, d, P)
print("행렬 P 출력")
printMatrix(P)
print("최소 곱셈 횟수: {}".format(result))
print("order(1,5) 출력: ", end="")
order(1, 5)

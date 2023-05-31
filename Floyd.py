# [문제] 최단경로 v3->v1 출력

def printMatrix(d):
    n = len(d[0])
    for i in range(1, n):
        for j in range(1, n):
            print("{0: < 5}".format(d[i][j]), end="  ")
        print()
    print()


def floyd(n, W, D, P):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            P[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            D[i][j] = W[i][j]

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if D[i][k] + D[k][j] < D[i][j]:
                    P[i][j] = k
                    D[i][j] = D[i][k] + D[k][j]
    print("행렬 W 출력")
    printMatrix(W)
    print("행렬 D 출력")
    printMatrix(D)


def path(q, r):
    if P[q][r] != 0:
        path(q, P[q][r])
        print("v{}".format(P[q][r]), end=" ")
        path(P[q][r], r)


inf = 1000
W = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 1, 5], [0, 9, 0, 3, inf, inf], [0, inf, inf, 0, 4, inf],
     [0, inf, inf, 2, 0, 3], [0, 3, inf, inf, inf, 0]]
D = [[0, 0, 0, 0, 0, 0] for i in range(6)]
P = [[0, 0, 0, 0, 0, 0] for i in range(6)]
print("Floyd 알고리즘 완성 및 최단경로 v3->v1 출력")
floyd(5, W, D, P)
print("행렬 P 출력")
printMatrix(P)
print("v3->v1 최단 경로 출력: ", end="")
path(3, 1)
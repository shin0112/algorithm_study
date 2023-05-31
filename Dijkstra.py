inf = 1000
n = 5
w = [[0, 7, 4, 6, 1], [inf, 0, inf, inf, inf], [inf, 2, 0, 5, inf],
     [inf, 3, inf, 0, inf], [inf, inf, inf, 1, 0]]
v = [False] * n
touch = n * [0]
save_length = n * [0]
dis = n * [inf]
f = []


def dijkstra(start):
    start -= 1
    i = 0
    index = 0
    for i in range(n):
        touch[i] = start
        dis[i] = w[start][i]
        save_length[i] = dis[i]
    v[start] = True

    for j in range(n - 1):
        min = inf
        for i in range(n):
            if 0 < dis[i] < min and not v[i]:
                min = dis[i]
                index = i
        v[index] = True

        e = (touch[index], index)
        f.append(e)

        for i in range(n):
            if (not v[i] and dis[index] + w[index][i] < dis[i]):
                dis[i] = dis[index] + w[index][i]
                touch[i] = index
            if 0 < dis[i] < save_length[i]:
                save_length[i] = dis[i]
        dis[index] = -1
    f.reverse()
    print(f)
    print(save_length)


dijkstra(1)

import sys

# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

INF = sys.maxsize
V, E = map(int, sys.stdin.readline().strip().split())
K = int(input())
graph = [[INF] * V for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u - 1][v - 1] = w


def dijkstra(K, V, graph):
    visit = [False] * V
    memory = [INF] * V
    memory[K - 1] = 0

    while True:
        m = INF
        N = -1

        for j in range(V):
            if not visit[j] and m > memory[j]:
                m = memory[j]
                N = j
        if m==INF:
            break

        for j in range(V):
            if visit[j]:continue
            via = memory[N]+graph[N][j]
            if memory[j]>via:
                memory[j]=visit

    return d


for d in dijkstra(K, V, graph):
    print(d if d != INF else 'INF')

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

# V : 정점의 개수
# E : 간선의 개수
V, E = map(int, sys.stdin.readline().strip().split())

# K : 시작할 정점
K = int(input())

# 가중치 그래프
graph = [[INF] * V for _ in range(V)]

# 정점 간 가중치 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u - 1][v - 1] = w


def dijkstra(K, V, graph):
    # 방문 여부
    visit = [False] * V

    # 정점 사이의 거리
    memory = [INF] * V

    # 출발 노드 초기화
    memory[K - 1] = 0

    while True:
        m = INF
        N = -1

        # 모든 정점을 순회
        for j in range(V):

            # 방문하지 않았고 거리가 더 짧으면
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

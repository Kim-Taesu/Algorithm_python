import heapq
import sys

from baek_joon.mst.config import *

INF = sys.maxsize


# 다익스트라 알고리즘
def dijkstra(start):
    distance = [INF] * len(graph_status)
    distance[start] = 0

    priority_queue = []
    heapq.heappush(priority_queue, [0, start])

    while priority_queue:
        # 거리가 제일 작은 노드 선택
        cur_dist, cur_node = heapq.heappop(priority_queue)

        # 인접 노드 iteration
        for dest, dest_dist in graph_status[cur_node].items():
            next_dist = distance[cur_node] + dest_dist
            if next_dist < distance[dest]:
                distance[dest] = next_dist
                heapq.heappush(priority_queue, [next_dist, dest])
    return distance


graph_status = [{} for _ in range(V)]
for DATA in DATA_LIST:
    u, v, w = DATA
    if v in graph_status[u]:
        graph_status[u][v] = min(graph_status[u][v], w)
    else:
        graph_status[u][v] = w

print('출발 노드:', K)
dist = dijkstra(K)
for d in dist:
    print(d if d != INF else "INF")



import heapq
import sys

INF = sys.maxsize


def dijkstra(status, K):
    distance = [INF] * (len(status))
    distance[K] = 0

    priority_queue = []
    heapq.heappush(priority_queue, [0, K])

    while priority_queue:
        cur_dist, cur_node = heapq.heappop(priority_queue)

        for dest, dest_dist in status[cur_node].items():
            next_dist = distance[cur_node] + dest_dist
            if next_dist < distance[dest]:
                distance[dest] = next_dist
                heapq.heappush(priority_queue, [next_dist, dest])
    return distance


V, E = map(int, input().strip().split())
K = int(input())
DATA_LIST = []
for _ in range(E):
    DATA_LIST.append(list(map(int, input().strip().split())))

graph_status = [{} for _ in range(V + 1)]

for DATA in DATA_LIST:
    u, v, w = DATA
    if v in graph_status[u]:
        graph_status[u][v] = min(graph_status[u][v], w)
    else:
        graph_status[u][v] = w
dist = dijkstra(graph_status, K)
for d in dist[1:]:
    print(d if d != INF else "INF")

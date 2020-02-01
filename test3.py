import heapq
import sys

INF = sys.maxsize


def prim(V, S, arr):
    queue = []
    node = []
    heapq.heappush(queue, (0, S))
    weight_sum = 0

    while len(node) < V:
        print(queue)
        print('\t', node)
        weight, start = heapq.heappop(queue)
        weight_sum += weight
        node.append(start)

        for i in range(V):
            if arr[start][i] != INF:
                if i in node:
                    continue
                else:
                    heapq.heappush(queue, (arr[start][i], i))
    return weight_sum


V = int(input().strip())
E = int(input().strip())
arr = [[INF] * V for _ in range(V)]
for _ in range(E):
    v, u, w = map(int, input().strip().split())
    arr[v - 1][u - 1] = w
    arr[u - 1][v - 1] = w

for v in range(V):
    print(v, prim(V, v, arr))

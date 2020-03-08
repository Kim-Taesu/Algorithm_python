import heapq

from basic.mst.config import *

E = len(DATA_LIST)
print('간선 개수:', E)
INF = -1
arr = [[INF] * V for _ in range(V)]
for DATA in DATA_LIST:
    x, y, w = DATA
    arr[x][y] = w
    arr[y][x] = w

print('출발 노드:', K)

heap = []
node = []

for a in arr:
    print(a)
print()

heapq.heappush(heap, (0, K))
weight_sum = 0
while not len(node) == V:
    print(heap)
    weight, start = heapq.heappop(heap)
    node.append(start)
    weight_sum += weight

    for i in range(V):
        if arr[start][i] != INF and not (i in node):
            heapq.heappush(heap, (arr[start][i], i))

print(node, weight_sum)

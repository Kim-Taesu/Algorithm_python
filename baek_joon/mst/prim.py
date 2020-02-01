import heapq
import sys

from baek_joon.mst.config import *

E = len(DATA_LIST)
print('간선 개수:', E)
INF = sys.maxsize
arr = [[INF] * V for _ in range(V)]
for DATA in DATA_LIST:
    x, y, w = DATA
    arr[x - 1][y - 1] = w
    arr[y - 1][x - 1] = w

print('출발 노드:', K)

heap = []
node = []

heapq.heappush(heap, (0, K))
weight_sum = 0
while not len(node) == V:
    weight, start = heapq.heappop(heap)
    node.append(start)
    weight_sum += weight

    for i in range(V):
        if arr[start][i] != INF and not (i in node):
            heapq.heappush(heap, (arr[start][i], i))

print(node, weight_sum)

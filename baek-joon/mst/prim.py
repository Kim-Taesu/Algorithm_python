# 실행 순서
# 1. 임의의 정점 선택 (정점 S)
# 2. 최초 정점으로부터 최소 비용의 정점을 선택 (최소 간선)
# 3. 2번에 연결된 모든 간선 중 가장 최소 비용의 간선을 선택하고 갱신

# 1 2 27
# 1 6 9
# 2 3 15
# 2 7 13
# 3 4 11
# 4 5 21
# 4 7 17
# 5 7 23
# 5 6 25


import heapq
import sys

input = sys.stdin.readline

V = 7
E = 9
INF = sys.maxsize

arr = [[INF] * V for _ in range(V)]

# 가중치 입력
for _ in range(E):
    x, y, w = map(int, input().strip().split())
    arr[x - 1][y - 1] = w
    arr[y - 1][x - 1] = w

S = 1 - 1

heap = []
node = []

heapq.heappush(heap, (0, S))

sum = 0
while not len(node) == V:
    weight, start = heapq.heappop(heap)
    node.append(start)
    sum += weight

    for i in range(V):
        if arr[start][i] != INF and not i in node:
            heapq.heappush(heap, (arr[start][i], i))

print(node, heap, sum)

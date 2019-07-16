import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = [[0] * m] * n
visit = [[0] * m] * n

wallCount = 3

for i in range(n):
    line = list(map(int, input().strip().split()))
    for j in range(m):
        arr[i][j] = line[j]
        if (line[j] == 2):
            visit[i][j]=2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, wallCount):
    queue = deque()
    queue.append((i, j, wallCount))
    while (queue):
        x, y, c = queue.popleft()

    pass


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            bfs(i, j, wallCount)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

arr = []
for _ in range(N):
    arr.append(list(input().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    result = 0
    queue = deque()
    queue.append((i, j))
    visit = [[-1] * M for _ in range(N)]
    visit[i][j] = 0
    while queue:
        cx, cy = queue.popleft()

        for q in range(4):
            nx = cx + dx[q]
            ny = cy + dy[q]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and visit[nx][ny] == -1 and arr[nx][ny] == 'L':
                queue.append((nx, ny))
                visit[nx][ny] = visit[cx][cy] + 1

    for i in visit:
        result = max(result, max(i))

    return result


sample = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            sample = max(sample, bfs(i, j))

print(sample)

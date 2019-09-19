import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
r1, c1, r2, c2 = map(int, input().strip().split())

arr = [[0] * N for _ in range(N)]
visit = [[False] * N for _ in range(N)]

queue = deque()
queue.append((r1, c1, 0))

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
visit[r1][c1] = True

while queue:
    cx, cy, count = queue.popleft()
    if cx == r2 and cy == c2:
        print(count)
        sys.exit(0)

    for i in range(len(dx)):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < N and not visit[nx][ny]:
            queue.append((nx, ny, count + 1))
            visit[nx][ny] = True
print(-1)
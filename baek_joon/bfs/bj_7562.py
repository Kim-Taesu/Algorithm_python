import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(int(input().strip())):
    N = int(input().strip())
    arr = [[0] * N for _ in range(N)]
    visit = [[False] * N for _ in range(N)]

    sx, sy = map(int, input().strip().split())
    ex, ey = map(int, input().strip().split())

    # bfs
    queue = deque()
    queue.append((sx, sy))

    while queue:
        # print(queue)
        cx, cy = queue.popleft()

        if visit[cx][cy]: continue
        if cx == ex and cy == ey:
            print(arr[cx][cy])
            break
        visit[cx][cy] = True

        for i in range(len(dx)):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N and not visit[nx][ny]:
                queue.append((nx, ny))
                arr[nx][ny] = arr[cx][cy] + 1

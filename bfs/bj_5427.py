from collections import deque
from sys import stdin

input = stdin.readline

R, C = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(R)]

visit = [[0] * C for _ in range(R)]

queue = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            sx, sy = i, j
        elif arr[i][j] == 'F':
            queue.append((i, j, 1))
            visit[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue.append((sx, sy, 0))
    visit[sx][sy] = 1

    while queue:
        x, y, f = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                if f: continue
                print(visit[x][y])
                return

            if not visit[nx][ny] and arr[nx][ny] !='#':
                queue.append((nx,ny,f))
                visit[nx][ny]=visit[x][y]+1

    print('IMPOSSIBLE')
    pass


bfs()

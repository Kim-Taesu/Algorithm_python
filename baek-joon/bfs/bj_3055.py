import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
water = deque()

R, C = map(int, input().strip().split())

arr = [list(input().strip()) for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            queue.append((i, j, 1))
            visit[i][j] = -1
        elif arr[i][j] == 'S':
            sx, sy = i, j

queue.append((sx, sy, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    # print(queue)
    # for z in arr:
    #     print(z)
    # print()
    # for z in visit:
    #     print(z)
    # print()

    x, y, f = queue.popleft()

    if arr[x][y] == 'D':
        if f == 1: continue
        print(visit[x][y])
        sys.exit(0)

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]

        if nx >= 0 and nx < R and ny >= 0 and ny < C and arr[nx][ny] != 'X':
            if f == 1:
                if arr[nx][ny] != 'D' and arr[nx][ny] != '*':
                    arr[nx][ny] = '*'
                    queue.append((nx, ny, 1))
            if f == 0:
                if arr[nx][ny] != '*' and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny, 0))

print('KAKTUS')

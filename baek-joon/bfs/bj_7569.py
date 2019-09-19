import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

zeroCount = 0
m, n, h = map(int, sys.stdin.readline().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

virus = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                virus.append((i, j, k))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]


while virus:
    x, y, z = virus.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dh[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
            continue
        if arr[nx][ny][nz]:
            continue
        arr[nx][ny][nz] = arr[x][y][z] + 1
        virus.append((nx, ny, nz))


def isCheck():
    result = 0
    for i in range(h):
        for j in range(n):
            if 0 in arr[i][j]:
                return -1
            result = max(result, max(arr[i][j]))
    return result - 1

print(isCheck())

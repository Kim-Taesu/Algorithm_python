import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

m, n, h = map(int, input().strip().split())

arr = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

virus = deque()

for q in range(h):
    for i in range(n):
        line = list(map(int, input().strip().split()))
        for j in range(m):
            arr[q][i][j] = line[j]
            if (line[j] == 1):
                virus.append((q, i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dh = [0, 1, -1]


def isRange(q, x, y):
    return q >= 0 and q < h and x >= 0 and x < n and y >= 0 and y < m


day = 0
allFine=True
while (virus):
    l = len(virus)
    day += 1
    while l > 0:
        he, x, y = virus.popleft()
        if visit[he][x][y] != 0:
            l -= 1
            continue
        visit[he][x][y] = 1
        for q in range(len(dh)):
            for i in range(len(dx)):
                nh = he + dh[q]
                nx = x + dx[i]
                ny = y + dy[i]
                if isRange(nh, nx, ny) and arr[nh][nx][ny] == 0:
                    allFine=False
                    arr[nh][nx][ny] = 1
                    virus.append((nh, nx, ny))

        l -= 1
    if allFine:
        day-=1
        break

def isCheck():
    for q in range(h):
        for i in range(n):
            for j in range(m):
                if arr[q][i][j]==0:
                    print(-1)
                    return

    print(day)
isCheck()

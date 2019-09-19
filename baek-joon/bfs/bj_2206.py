import sys
from collections import deque

INF = 987654321
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().strip().split(' '))
arr = [list(input()) for _ in range(n)]
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def isRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < m


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visit[0][0][0] = 1

    while (queue):
        x, y, crush = queue.popleft()

        if x == n - 1 and y == m - 1:
            print(visit[x][y][crush])
            return

        for i in range(len(dx)):
            newX = x + dx[i]
            newY = y + dy[i]

            if isRange(newX, newY) == False: continue

            if visit[newX][newY][crush]: continue

            if arr[newX][newY] == '0':
                visit[newX][newY][crush] = visit[x][y][crush] + 1
                queue.append((newX, newY, crush))

            if arr[newX][newY] == '1' and crush == 0:
                visit[newX][newY][1] = visit[x][y][crush] + 1
                queue.append((newX, newY, 1))
    print(-1)


bfs()

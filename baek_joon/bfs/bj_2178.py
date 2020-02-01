import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().strip().split())
arr = [[0 for i in range(m)] for j in range(n)]
visit = [[0 for i in range(m)] for j in range(n)]

X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]

for i in range(n):
    line = list(map(int, list(sys.stdin.readline().strip())))
    arr[i] = line

queue = deque()
queue.append((0, 0))


def isRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < m


while (queue):
    x, y = queue.popleft()

    visit[x][y] += 1
    for i in range(len(X)):
        newX = x + X[i]
        newY = y + Y[i]
        if (isRange(newX, newY) and arr[newX][newY] == 1 and visit[newX][newY] == 0):
            visit[newX][newY] += visit[x][y]
            queue.append((newX, newY))

print(visit[x][y])

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]

m, n = map(int, sys.stdin.readline().strip().split())
queue = deque()
arr = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(len(line)):
        arr[i][j] = line[j]
        if (arr[i][j] == 1): queue.append((i, j))


def isOk(x, y):
    return x >= 0 and x < n and y >= 0 and y < m and arr[x][y] == 0


day = 0

while (queue):
    # print(queue)
    # for i in arr:
    #     print(i)
    # print()
    for i in range(len(queue)):
        x, y = queue.popleft()
        for j in range(len(X)):
            newX = x + X[j]
            newY = y + Y[j]
            if (isOk(newX, newY)):
                queue.append((newX, newY))
                arr[newX][newY] = 1

    day += 1

for i in arr:
    if (0 in i):
        print(-1)
        exit(0)

print(day - 1)

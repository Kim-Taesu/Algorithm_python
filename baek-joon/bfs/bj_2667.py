import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    line = list(map(int, list(sys.stdin.readline().strip())))
    for j in range(n):
        arr[i][j] = line[j]

result = []
X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]


def isOK(x, y):
    return x >= 0 and x < n and y >= 0 and y < n and arr[x][y] == 1


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    count = 0
    arr[i][j] = -1
    while (queue):
        print(queue)
        x, y = queue.popleft()
        count += 1
        for i in range(len(X)):
            newX = x + X[i]
            newY = y + Y[i]
            if (isOK(newX, newY)):
                queue.append((newX, newY))
                arr[newX][newY] = -1

    result.append(count)
    print()
    pass


for i in range(n):
    for j in range(n):
        if (arr[i][j] == 1):
            bfs(i, j)

result.sort()
print(len(result))
for i in result: print(i)

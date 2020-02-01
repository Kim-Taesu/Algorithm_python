import sys

sys.setrecursionlimit(10000)

t = int(sys.stdin.readline().strip())

X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]

count = 0


def dfs(x, y):
    arr[x][y] = -1
    for z in range(len(X)):
        newX = x + X[z]
        newY = y + Y[z]

        if (newX >= 0 and newX < n and newY >= 0 and newY < m and arr[newX][newY] == 1):
            dfs(newX, newY)
    pass


for z in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    arr = [[0 for i in range(m)] for j in range(n)]

    for i in range(k):
        y, x = map(int, sys.stdin.readline().strip().split())
        arr[x][y] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if (arr[i][j] == 1):
                dfs(i, j)
                count += 1

    print(count)

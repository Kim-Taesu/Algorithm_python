import sys

sys.setrecursionlimit(10 ** 6)

line = sys.stdin.readline().strip().split(' ')
m, n = int(line[0]), int(line[1])

X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]
dp = [[0 for i in range(n)] for j in range(m)]
arr = [[0 for i in range(n)] for j in range(m)]
count = 0
for i in range(m):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))


def isRange(x, y):
    return x >= 0 and x < m and y >= 0 and y < n


def go(x, y, value):
    if (x == m - 1 and y == n - 1):
        for i in dp:
            print(i)
        print()
        global count
        count += 1
        return

    if (dp[x][y] == 0):
        dp[x][y] += value
        for i in range(4):
            newX = x + X[i]
            newY = y + Y[i]

            if (isRange(newX, newY) == False): continue
            if (arr[x][y] > arr[newX][newY]):
                go(newX, newY, 1)

    return


for i in dp:
    print(i)
print()

go(0, 0, 0)
print(count)

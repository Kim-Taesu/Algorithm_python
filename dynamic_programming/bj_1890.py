import sys

sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline().strip())

dp = [[-1 for i in range(N)] for j in range(N)]
arr = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))


def isRange(x, y):
    return x >= 0 and x < N and y >= 0 and y < N


def printDp():
    for i in dp:
        print(i)
    print()


def go(x, y):
    if (x == 0 and y == 0):
        return 1

    if (dp[x][y] == -1):
        dp[x][y] = 0

        for i in range(x):
            if (x == i + arr[i][y]):
                dp[x][y] += go(i, y)

        for i in range(y):
            if (y == i + arr[x][i]):
                dp[x][y] += go(x, i)

    return dp[x][y]



print(go(N - 1, N - 1))

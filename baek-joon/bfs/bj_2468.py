import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input().strip())

arr = [[0 for _ in range(n)] for _ in range(n)]

maxValue = 0
minValue = 987654321

for i in range(n):
    line = list(map(int, input().strip().split()))
    for j in range(n):
        arr[i][j] = line[j]
        if maxValue < line[j]: maxValue = line[j]
        if minValue > line[j]: minValue = line[j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# print(minValue,maxValue)

def isRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def dfs(i, j, h):
    if not isRange(i, j): return

    if visit[i][j] or arr[i][j] <= h: return

    visit[i][j] = True

    for z in range(4):
        newX = i + dx[z]
        newY = j + dy[z]

        dfs(newX, newY, h)


pass

maxCount = 0
for h in range(0, maxValue + 1):
    visit = [[False for _ in range(n)] for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(n):
            if (arr[i][j] > h and not visit[i][j]):
                dfs(i, j, h)
                count += 1
    # print(count)
    maxCount = max(maxCount, count)

print(maxCount)

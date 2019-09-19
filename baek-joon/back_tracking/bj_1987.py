import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

R, C = map(int, input().strip().split())

INF = R * C

arr = [[0] * C for _ in range(R)]
visit = [False] * 26
for i in range(R):
    line = list(input().strip())
    for j in range(C):
        arr[i][j] = ord(line[j]) - 65

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

walk = 1
wTmp = 1
start = arr[0][0]


def dfs(x, y, w):
    visit[arr[x][y]] = True
    global walk
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < R and ny >= 0 and ny < C and not visit[arr[nx][ny]]:
            walk = max(walk, w + 1)
            dfs(nx, ny, w + 1)

    visit[arr[x][y]] = False
visit[arr[0][0]] = True
dfs(0, 0, 1)

print(walk)

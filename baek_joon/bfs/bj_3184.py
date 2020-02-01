from collections import deque

R, C = map(int, input().strip().split(' '))

arr = []

visit = [[False] * C for _ in range(R)]

for i in range(R):
    line = list(input().strip())
    arr.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

totalSheep = 0
totalWolf = 0


def bfs(x, y):
    global visit, totalWolf, totalSheep
    visit[x][y] = True
    sheep = 0
    wolf = 0

    if arr[x][y] == 'o':
        sheep += 1
    elif arr[x][y] == 'v':
        wolf += 1

    queue = deque()
    queue.append((x, y))

    while queue:
        i, j = queue.popleft()
        for z in range(4):
            ni = i + dx[z]
            nj = j + dy[z]

            if ni < 0 or ni >= R or nj < 0 or nj >= C: continue
            if visit[ni][nj]: continue
            if arr[ni][nj] == '#': continue

            visit[ni][nj] = True
            if arr[ni][nj] == 'o': sheep += 1
            if arr[ni][nj] == 'v': wolf += 1
            queue.append((ni, nj))

    if sheep > wolf:
        totalSheep += sheep
    else:
        totalWolf += wolf


for i in range(R):
    for j in range(C):
        if arr[i][j] != '#' and not visit[i][j]:
            bfs(i, j)

print(totalSheep, totalWolf)

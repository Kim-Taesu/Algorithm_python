n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
v, safe, virus = [], -3, 100


def dfs(x, y):
    res = 1
    c[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not (c[nx][ny] or a[nx][ny]):
            res += dfs(nx, ny)
    return res


def solve(wall, x, y):
    global virus, c
    if wall == 3:
        cnt = 0
        c = [[False] * m for _ in range(n)]
        for i, j in v:
            cnt += dfs(i, j)
        virus = min(virus, cnt)
        return
    for i in range(x, n):
        for j in range(0, m):
            if a[i][j] == 0:
                a[i][j] = 1
                solve(wall + 1, i, j + 1)
                a[i][j] = 0


for i in range(n):
    for j in range(m):
        if a[i][j] != 1:
            safe += 1
        if a[i][j] == 2:
            v.append((i, j))
solve(0, 0, 0)
print(safe - virus)

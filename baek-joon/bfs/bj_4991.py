import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0: break

    arr = [[0] * w for _ in range(h)]
    visit = [[[0 for _ in range(1 << 11)] for _ in range(w)] for _ in range(h)]

    virus = 0
    queue = deque()

    for i in range(h):
        line = list(input().strip())
        for j in range(w):
            if line[j] == 'o':
                queue.append((0, i, j))
            elif line[j] == '*':
                virus += 1
                arr[i][j] = virus
            elif line[j] == 'x':
                arr[i][j] = -1

    flag = (1 << virus) - 1
    check = 0

    while queue:
        d, x, y = queue.popleft()

        if d == flag:
            print(visit[x][y][d])
            check = -1
            break

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if nx >= 0 and nx < h and ny >= 0 and ny < w and arr[nx][ny] != -1:
                if (arr[nx][ny] > 0):

                    if not visit[nx][ny][d | (1 << (arr[nx][ny] - 1))]:
                        queue.append((d | (1 << (arr[nx][ny] - 1)), nx, ny))
                        visit[nx][ny][d | (1 << (arr[nx][ny] - 1))] = visit[x][y][d] + 1;

                if (arr[nx][ny] == 0):

                    if not visit[nx][ny][d]:
                        queue.append((d, nx, ny));
                        visit[nx][ny][d] = visit[x][y][d] + 1;
    if check == 0:
        print(-1)

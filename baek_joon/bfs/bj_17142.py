import sys
from collections import deque

N, M = map(int, input().strip().split(' '))

arr = [[0] * N for _ in range(N)]
virus = []
blank = []
for i in range(N):
    line = list(map(int, input().strip().split(' ')))
    for j in range(N):
        arr[i][j] = line[j]
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 0:
            blank.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(cur_virus):
    queue = deque()
    visit = [[0] * N for _ in range(N)]
    cur_blank = []

    for v in virus:
        cur_x, cur_y = v
        if (cur_x, cur_y) in cur_virus:
            visit[cur_x][cur_y] = 3
            queue.append((cur_x, cur_y, 0))
        else:
            visit[cur_x][cur_y] = 2
    time = -1
    while queue:
        cx, cy, ct = queue.popleft()

        if ct != time:
            if len(cur_blank) == len(blank):
                global min_value
                min_value = min(min_value, time + 1)
                return
            else:
                time += 1

        visit[cx][cy] = 3

        for z in range(4):
            nx, ny = cx + dx[z], cy + dy[z]

            if 0 <= nx < N and 0 <= ny < N:
                # 방문하지 않았고 벽이 아니면
                if visit[nx][ny] == 0:
                    # 빈칸이면
                    if arr[nx][ny] == 0:
                        cur_blank.append((nx, ny))
                        visit[nx][ny] = 3
                        queue.append((nx, ny, ct + 1))

                    # 비활성 바이러스이면
                    if arr[nx][ny] == 2:
                        visit[nx][ny] = 3
                        queue.append((nx, ny, ct + 1))
                # 방문 했으면
                else:
                    if visit[nx][ny] == 2:
                        queue.append((nx, ny, ct + 1))


min_value = sys.maxsize


def dfs(cur_virus, index):
    if len(cur_virus) == M:
        # print(cur_virus)
        bfs(cur_virus)
        return

    for i in range(index, len(virus)):
        cur_virus.append(virus[i])
        dfs(cur_virus, i + 1)
        cur_virus.pop()


dfs([], 0)
print(min_value if min_value != sys.maxsize else -1)

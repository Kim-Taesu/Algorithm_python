from collections import deque

N, L, R = map(int, input().strip().split(' '))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    values = [arr[i][j]]
    locations = [(i, j)]
    visit[i][j] = True

    while queue:
        cx, cy = queue.popleft()

        for z in range(4):
            nx, ny = cx + dx[z], cy + dy[z]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visit[nx][ny]:
                continue

            if L <= abs(arr[cx][cy] - arr[nx][ny]) <= R:
                visit[nx][ny] = True
                values.append(arr[nx][ny])
                queue.append((nx, ny))
                locations.append((nx, ny))

    return locations, sum(values) // len(values)


move_count = 0

while True:

    is_move = False
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                locations, result = bfs(i, j)
                if len(locations) > 1:
                    is_move = True
                    for location in locations:
                        lx, ly = location
                        arr[lx][ly] = result

    if is_move:
        move_count += 1
    else:
        break

print(move_count)

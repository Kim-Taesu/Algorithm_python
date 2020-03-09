import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visit = [[False] * C for _ in range(R)]
total_sheep = 0
total_wolf = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] != '#' and not visit[i][j]:
            queue = deque()
            queue.append((i, j))
            visit[i][j] = True
            wolf_count = 0
            sheep_count = 0
            while queue:
                cx, cy = queue.popleft()

                if arr[cx][cy] == 'k':
                    sheep_count += 1

                if arr[cx][cy] == 'v':
                    wolf_count += 1

                for z in range(len(dx)):
                    nx, ny = cx + dx[z], cy + dy[z]

                    if 0 <= nx < R and 0 <= ny < C and \
                            not visit[nx][ny] and \
                            arr[nx][ny] != '#':
                        visit[nx][ny] = True
                        queue.append((nx, ny))
            if sheep_count > wolf_count:
                total_sheep += sheep_count
            else:
                total_wolf += wolf_count
print(total_sheep, total_wolf)

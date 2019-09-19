import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input().strip())
arr = []
for _ in range(N):
    arr.append(list(input().strip()))

visit1 = [[0] * N for _ in range(N)]
visit2 = [[0] * N for _ in range(N)]

count1 = 0
count2 = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs2(i, j, k, c):
    queue = deque()
    queue.append((i, j))
    visit2[i][j] = c
    while queue:
        cx, cy = queue.popleft()

        for q in range(4):
            nx = cx + dx[q]
            ny = cy + dy[q]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and visit2[nx][ny] == 0:
                if arr[nx][ny] == k or (k == 'G' and arr[nx][ny] == 'R') or (k == 'R' and arr[nx][ny] == 'G'):
                    queue.append((nx, ny))
                    visit2[nx][ny] = c
    pass


def bfs1(i, j, k, c):
    queue = deque()
    queue.append((i, j))
    visit1[i][j] = c
    while queue:
        cx, cy = queue.popleft()

        if visit2[cx][cy] == 0:
            visit2[cx][cy] = count2
        for q in range(4):
            nx = cx + dx[q]
            ny = cy + dy[q]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and visit1[nx][ny] == 0:
                if arr[nx][ny] == k:
                    queue.append((nx, ny))
                    visit1[nx][ny] = c
                elif (k == 'R' and arr[nx][ny] == 'G') or (k == 'G' and arr[nx][ny] == 'R') and visit2[nx][ny] == 0:
                    bfs2(nx, ny, arr[nx][ny], count2)
    pass


for i in range(N):
    for j in range(N):
        if visit1[i][j] == 0:
            count1 += 1
            if visit2[i][j] == 0:
                count2 += 1
            bfs1(i, j, arr[i][j], count1)

print(count1, count2)
#
# for i in visit2:
#     print(i)

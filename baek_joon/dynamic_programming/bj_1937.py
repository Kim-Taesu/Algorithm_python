import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
arr = []
info = []
for i in range(n):
    line = list(map(int, input().strip().split()))
    arr.append(line)
    for j in range(n):
        info.append((line[j], i, j))
info = sorted(info, key=lambda x: -x[0])

dp = [[1] * n for _ in range(n)]
max_value = 1
for item in info:
    bamboo, i, j = item
    queue = deque()
    queue.append((i, j))
    while queue:
        cx, cy = queue.popleft()
        for z in range(4):
            nx, ny = cx + dx[z], cy + dy[z]

            if 0 <= nx < n and 0 <= ny < n and \
                    arr[cx][cy] < arr[nx][ny]:
                dp[cx][cy] = max(dp[cx][cy], dp[nx][ny] + 1)
    max_value = max(max_value, dp[i][j])
print(max_value)

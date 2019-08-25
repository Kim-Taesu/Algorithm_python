import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().strip().split())
INF = 987654321

arr = [[INF] * N for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().strip().split())
    arr[i - 1][j - 1] = 1
    arr[j - 1][i - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] != INF and arr[k][j] != INF:
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

winner = (-1, INF)

for i in range(len(arr)):
    score = 0
    for j in range(len(arr)):
        if i == j: continue
        score += arr[i][j]
    if winner[1] > score:
        winner = (i, score)

print(winner[0] + 1)

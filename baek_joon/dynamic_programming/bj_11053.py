import sys

n = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().strip().split()))

visit = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if (line[i] > line[j] and visit[i] < visit[j] + 1):
            visit[i] = visit[j] + 1
print(max(visit))

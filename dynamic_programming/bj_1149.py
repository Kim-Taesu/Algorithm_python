import sys

INF = 987654321
n = int(sys.stdin.readline().strip())

cost = []
dp = [[0 for i in range(3)] for i in range(n)]
for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    cost.append(line)

dp[0] = cost[0]

for q in range(1, n):
    result = INF

    for i in range(3):
        costI = cost[q][i]
        in1 = costI + dp[q - 1][int((i + 1) % 3)]
        in2 = costI + dp[q - 1][int((i + 2) % 3)]
        dp[q][i] = min(in1, in2)

print(min(dp[n-1]))

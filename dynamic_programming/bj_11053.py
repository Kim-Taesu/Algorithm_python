import sys

n = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().strip().split()))

dp = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if (line[i] > line[j] and dp[i] < dp[j] + 1):
            dp[i] = dp[j] + 1
print(max(dp))

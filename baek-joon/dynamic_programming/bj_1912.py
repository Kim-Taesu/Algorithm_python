import sys

n = int(sys.stdin.readline())

line = list(map(int, sys.stdin.readline().strip().split(' ')))
print(line)

dp = [0 for i in range(len(line))]
dp[0] = line[0]

for i in range(1, len(line)):
    dp[i] = line[i]
    if (dp[i] < dp[i - 1] + dp[i]):
        dp[i] = dp[i - 1] + dp[i]

print(dp)
print(max(dp))

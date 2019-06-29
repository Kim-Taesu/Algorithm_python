import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    num = int(sys.stdin.readline().strip())
    dp = [0 for i in range(11 + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp, dp[num])

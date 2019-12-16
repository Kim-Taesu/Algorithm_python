import sys

sys.setrecursionlimit(10 ** 6)

T = int(sys.stdin.readline().strip())
for z in range(T):
    q = int(sys.stdin.readline().strip())
    dp = [0 for i in range(q + 1)]
    dp[0] = 0
    if (q == 1 or q == 2):
        print(1)
        continue

    dp[1] = 1
    dp[2] = 1

    for i in range(3, q + 1):
        dp[i] = dp[i - 3] + dp[i - 2]

    print(dp[q])

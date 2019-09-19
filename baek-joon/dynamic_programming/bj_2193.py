import sys

n = int(sys.stdin.readline().strip())

if (n == 1 or n == 2):
    print(1)

else:
    dp = []
    dp.append(0)
    dp.append(1)
    dp.append(1)
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
        if(i==n):
            print(dp[n])
            break

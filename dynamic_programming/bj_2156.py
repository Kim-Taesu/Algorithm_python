import sys

n = int(sys.stdin.readline().strip())

arr = [0 for i in range(n + 1)]
dp = [0 for i in range(n + 1)]

for i in range(n):
    arr[i + 1] = int(sys.stdin.readline().strip())

if(n==1):
    print(arr[1])
else:

    dp[1] = arr[1]
    dp[2] = dp[1] + arr[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i], dp[i-1])


    print(dp[n])
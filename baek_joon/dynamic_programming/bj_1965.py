n = int(input())
arr = list(map(int, input().strip().split(' ')))
dp = [False] * len(arr)

dp[0] = 1
result = 0
for i in range(n):
    max_value = 0
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and dp[j] > max_value:
            max_value = dp[j]
    dp[i] = max_value + 1
    result = max(result, dp[i])
print(result)

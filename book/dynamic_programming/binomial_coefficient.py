n, r = map(int, input().strip().split(' '))

dp = [[-1] * r for _ in range(n)]


def dfs(n, r):
    # 기저 사례
    if r == 0 or n == r: return 1

    # 캐쉬 저장 여부 확인
    if dp[n][r] != -1: return dp[n][r]

    # 캐쉬 저장
    dp[n][r] = dfs(n - 1, r - 1) + dfs(n - 1, r)

    # 값 리턴
    return dp[n][r]


print(dfs(n - 1, r - 1))

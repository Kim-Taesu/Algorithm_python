S, A, B, C = map(int, input().strip().split(' '))

dp = [[[[-1] * 51 for _ in range(51)] for _ in range(51)] for _ in range(51)]


def dfs(s, a, b, c):
    global dp, A, B, C
    # 기저 사례
    if s == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0

    if a < 0 or b < 0 or c < 0: return 0

    # 캐쉬 체크
    if dp[s][a][b][c] != -1: return dp[s][a][b][c]

    # 캐쉬 저장
    dp[s][a][b][c] = 0 \
                     + dfs(s - 1, a - 1, b, c) \
                     + dfs(s - 1, a, b - 1, c) \
                     + dfs(s - 1, a, b, c - 1) \
                     + dfs(s - 1, a - 1, b - 1, c) \
                     + dfs(s - 1, a - 1, b, c - 1) \
                     + dfs(s - 1, a, b - 1, c - 1) \
                     + dfs(s - 1, a - 1, b - 1, c - 1)

    return dp[s][a][b][c] % 1000000007


print(dfs(S, A, B, C))

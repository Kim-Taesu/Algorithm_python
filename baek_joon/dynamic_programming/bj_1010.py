T = int(input())


def dfs(N, M):
    # 기저 사례1 : N이 M보다 클수는 없으므로
    if N > M:
        return 0
    # 기저 사례2 : N이 1개이면 경우의수는 M가지 이다.
    if N == 0:
        return dp[N][M]

    # 메모제이션 확인
    if dp[N][M] != 0:
        return dp[N][M]

    # 메모제이션
    for i in range(1, M + 1):
        dp[N][M] += dfs(N - 1, M - i)

    return dp[N][M]


for _ in range(T):
    N, M = map(int, input().strip().split(' '))
    dp = [[0] * M for _ in range(N)]
    for i in range(M):
        dp[0][i] = i + 1
    print(dfs(N - 1, M - 1))

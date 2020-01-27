import sys

sys.setrecursionlimit(10 ** 6)

n, r = map(int, input().strip().split(' '))

visit = [[-1] * r for _ in range(n)]


def dfs(n, r):
    # 기저 사례
    if r == 0 or n == r: return 1

    # 캐쉬 저장 여부 확인
    if visit[n][r] != -1: return visit[n][r]

    # 캐쉬 저장
    visit[n][r] = dfs(n - 1, r - 1) + dfs(n - 1, r)

    # 값 리턴
    return visit[n][r]


print(dfs(n - 1, r - 1))

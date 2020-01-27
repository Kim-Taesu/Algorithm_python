import sys

N = int(input())
hp = [0] * 3
index = 0
for i in input().strip().split(' '):
    hp[index] = int(i)
    index += 1
visit = [[[-1] * 61 for _ in range(61)] for _ in range(61)]


def dfs(a, b, c):
    # print(a, b, c)

    # 기저 사례
    if a == 0 and b == 0 and c == 0: return 0

    # 캐쉬 체크
    if visit[a][b][c] != -1: return visit[a][b][c]

    # 기능 구현 및 캐쉬 저장
    visit[a][b][c] = sys.maxsize
    visit[a][b][c] = min(visit[a][b][c], dfs(max(0, a - 9), max(0, b - 3), max(0, c - 1)) + 1)
    visit[a][b][c] = min(visit[a][b][c], dfs(max(0, a - 9), max(0, b - 1), max(0, c - 3)) + 1)

    visit[a][b][c] = min(visit[a][b][c], dfs(max(0, a - 3), max(0, b - 9), max(0, c - 1)) + 1)
    visit[a][b][c] = min(visit[a][b][c], dfs(max(0, a - 1), max(0, b - 9), max(0, c - 3)) + 1)

    visit[a][b][c] = min(visit[a][b][c], dfs(max(0, a - 3), max(0, b - 1), max(0, c - 9)) + 1)
    visit[a][b][c] = min(visit[a][b][c], dfs(max(0, a - 1), max(0, b - 3), max(0, c - 9)) + 1)

    return visit[a][b][c]


# 1 hp, 2 hp, 3 hp, count
print(dfs(hp[0], hp[1], hp[2]))

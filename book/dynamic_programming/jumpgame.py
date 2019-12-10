7
2516141
6112293
7232131
1131712
4123412
3312341
1529480

n = int(input().strip())

arr = []
dp = [[-1] * n for _ in range(n)]
for _ in range(n):
    arr.append(list(input().strip()))


def dfs(i, j):
    # 기저사례
    if i == n - 1 and j == n - 1:
        print('find!')
        return 1

    # 범위 체크
    if i < 0 or i >= n or j < 0 or j >= n: return 0

    # 캐쉬 저장 여부 확인
    if dp[i][j] != -1: return dp[i][j]

    # 캐쉬 저장
    dp[i][j] = dfs(i + int(arr[i][j]), j) + dfs(i, j + int(arr[i][j]))

    return dp[i][j]


result = dfs(0, 0)

if result > 0:
    print(result)
else:
    print(-1)

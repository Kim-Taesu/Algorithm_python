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
visit = [[False] * n for _ in range(n)]
for _ in range(n):
    arr.append(list(input().strip()))


def dfs(i, j):
    print(i, j)
    global arr
    # 기저사례
    if i == n - 1 and j == n - 1:
        return True
    if i >= n or j >= n:
        return False

    # 캐쉬 저장 여부 확인
    if visit[i][j]:
        return visit[i][j]

    # 캐쉬 저장
    else:
        visit[i][j] = dfs(i + int(arr[i][j]), j) or dfs(i, j + int(arr[i][j]))
        return visit[i][j]


sample = dfs(0, 0)

if sample > 0:
    print(sample)
else:
    print(-1)

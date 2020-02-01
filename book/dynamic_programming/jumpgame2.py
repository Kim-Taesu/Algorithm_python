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
visit = [[-1] * n for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, list(input().strip()))))


def dfs(i, j):
    global arr
    # 기저사례
    if i == n - 1 and j == n - 1:
        return arr[i][j]
    if i >= n or j >= n:
        return -1

    # 캐쉬 저장 여부 확인
    if visit[i][j] != -1:
        return visit[i][j]

    # 캐쉬 저장
    else:
        tmp = max(dfs(i + int(arr[i][j]), j), dfs(i, j + int(arr[i][j])))
        if tmp != -1:
            visit[i][j] = arr[i][j] + tmp
            return visit[i][j]
        else:
            return -1


visit[n - 1][n - 1] = arr[n - 1][n - 1]
sample = dfs(0, 0)

if sample > 0:
    print(sample)
else:
    print(-1)

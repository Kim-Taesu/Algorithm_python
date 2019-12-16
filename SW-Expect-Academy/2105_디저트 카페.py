dx = [-1, -1, 1, 1]
dy = [-1, 1, 1, -1]

T = int(input())

visit = []
si, sj = 0, 0


def go(i, j, val):
    global N, arr, visit, si, sj, result
    # print(i, j, val)

    for z in range(4):
        ni = i + dx[z]
        nj = j + dy[z]

        if ni == si and nj == sj and len(val) > 2:
            # print('+find', val)
            result = max(result, len(val))
            continue

        if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and arr[ni][nj] not in val:
            visit[ni][nj] = True
            val.append(arr[ni][nj])
            go(ni, nj, val)
            visit[ni][nj] = False
            val.pop()
            pass

    pass


for test_case in range(1, T + 1):
    result = -1
    N = int(input())

    arr = []

    for i in range(N):
        line = list(map(int, input().strip().split(' ')))
        arr.append(line)

    for i in range(N):
        for j in range(N):
            # print('start',i,j)
            visit = [[False] * N for _ in range(N)]
            si, sj = i, j
            go(i, j, [arr[i][j]])

    print('#%d %d' % (test_case, result))

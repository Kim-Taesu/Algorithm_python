N, K = map(int, input().strip().split(' '))

arr = [[[[False] * 450 for _ in range(31)] for _ in range(31)] for _ in range(31)]
line = [0] * 32


def solve(n, a, b, k):
    global N, K, line
    # print(n, a, b, k, line)
    if n == N:
        if k == K:
            return True
        else:
            return False

    # 방문 체크
    if arr[n][a][b][k]:
        return False
    arr[n][a][b][k] = True

    line[n] = ('A')
    if solve(n + 1, a + 1, b, k): return True

    line[n] = 'B'
    if solve(n + 1, a, b + 1, k + a): return True

    line[n] = 'C'
    if solve(n + 1, a, b, k + a + b): return True

    return False


if solve(0, 0, 0, 0):
    for l in line:
        if l != 0: print(l, end='')
else:
    print(-1)

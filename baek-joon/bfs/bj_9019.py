from collections import deque

N, M, C = 10000, 1000, "DSLR"
visit = [0] * N
cmd = [0] * N

for _ in range(int(input())):
    A, B = map(int, input().split())
    check = [False] * N
    q = deque()
    q.append(A)
    while q:
        x = q.popleft()
        if x == B:
            v = []
            while x != A:
                v.append(cmd[x])
                x = visit[x]
            print(''.join(map(str, v[::-1])))
            break
        nx = (x * 2 % N, x - 1 if x else N - 1, x % M * 10 + x // M, x // 10 + x % 10 * M)
        for i in range(4):
            if not check[nx[i]]:
                check[nx[i]] = True
                visit[nx[i]] = x
                cmd[nx[i]] = C[i]
                q.append(nx[i])


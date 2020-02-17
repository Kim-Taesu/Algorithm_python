N, M, K = map(int, input().split())  # n:n*n, m개 나무 k년
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

arr = [[5] * N for _ in range(N)]

di = [[-1, 0], [0, -1], [1, 0], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
for _ in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            if len(tree[i][j]) <= 0: continue
            tree[i][j].sort()
            idx = 0
            while idx < len(tree[i][j]):
                if tree[i][j][idx] <= arr[i][j]:
                    arr[i][j] -= tree[i][j][idx]
                    tree[i][j][idx] += 1
                    idx += 1
                else:
                    die = tree[i][j][idx:]
                    for now in die:  # 죽은나무!
                        arr[i][j] += (now // 2)
                    tree[i][j] = tree[i][j][:idx]
                    break

    # 가을
    for i in range(N):
        for j in range(N):
            c = 0
            if tree[i][j]:
                for now in tree[i][j]:
                    if now % 5 == 0:
                        c += 1
            if c > 0:
                for z in range(8):
                    ni = i + di[z][0]
                    nj = j + di[z][1]
                    if 0 <= ni < N and 0 <= nj < N:
                        for _ in range(c):
                            tree[ni][nj].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += A[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)

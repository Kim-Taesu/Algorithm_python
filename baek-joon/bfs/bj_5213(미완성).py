from collections import deque

N = int(input())

arr = [[0] * (N * 2) for _ in range(N)]
visit = [[False] * (N * 2) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

index = 0
row = 0
for i in range(N * N - N // 2):
    ai, bi = map(int, input().strip().split(' '))

    if row % 2 != 0 and index == 0:
        arr[row][index] = -1
        index += 1

    arr[row][index] = ai
    arr[row][index + 1] = bi
    index += 2

    if row % 2 == 0 and index == N * 2:
        row += 1
        index = 0

    if row % 2 != 0 and index == (N * 2) - 1:
        arr[row][index] = -1
        row += 1
        index = 0

queue = deque()

# i, j, count
queue.append((0, 0, 0, []))

visit[0][0] = True

while queue:
    i, j, c, line = queue.popleft()

    if i == N - 1:
        print(c)
        print(line)

    for z in range(4):
        ni, nj = i + dx[z], j + dy[z]

        if not (0 <= ni < N and 0 <= nj < N * 2): continue
        if arr[ni][nj] == -1: continue

        queue.append(())

    # 짝수
    if i % 2 == 0:
        if j % 2 == 0:

            pass
        else:
            pass
        pass

    # 홀수
    else:
        if j % 2 != 0:
            pass
        else:
            pass
        pass

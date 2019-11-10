import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().strip().split(' '))

arr = [[0] * M for _ in range(N)]

for i in range(N):
    line = list(map(int, input().strip().split(' ')))
    for j in range(len(line)):
        arr[i][j] = line[j]

arr[x][y] = 0

move = list(map(int, input().strip().split(' ')))
# 위 오 왼 앞 뒤 아
dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for m in move:
    nx, ny = x + dx[m - 1], y + dy[m - 1]

    if not (0 <= nx <= N - 1 and 0 <= ny <= M - 1):
        continue

    # 주사위 이동
    # 좌우 이동
    if m < 3:
        # 우
        if m == 1:
            # 앞 뒤 가만히
            tmp = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = dice[1]
            dice[1] = tmp
            pass
        # 좌
        if m == 2:
            tmp = dice[0]
            dice[0] = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[2]
            dice[2] = tmp
            pass

    else:
        # 북
        if m == 3:
            # 앞 뒤 가만히
            tmp = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[5]
            dice[5] = dice[4]
            dice[4] = tmp
            pass

        # 좌
        if m == 4:
            tmp = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[5]
            dice[5] = dice[3]
            dice[3] = tmp
            pass

    # 위아래 이동

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
        pass

    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0
        pass

    print(dice[0])

    x, y = nx, ny

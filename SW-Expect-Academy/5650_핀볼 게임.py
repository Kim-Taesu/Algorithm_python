T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
blackHole = []
warmHole = {}
arr = []


def find(shpae, i, j, bx, by):
    if shpae == 1:
        # 위로 올라감, 아래로 반사
        if bx == -1 and by == 0:
            return i, j, 1, 0
        # 아래로 내려감, 오른쪽으로 반사
        if bx == 1 and by == 0:
            return i, j, 0, 1
        # 왼쪽으로, 위로 반사
        if bx == 0 and by == -1:
            return i, j, -1, 0
        # 오른쪽으로, 왼쪽 반사
        if bx == 0 and by == 1:
            return i, j, 0, -1

    if shpae == 2:
        # 위로 올라감, 오른쪽으로
        if bx == -1 and by == 0:
            return i, j, 0, 1
        # 아래로 내려감, 위로반사
        if bx == 1 and by == 0:
            return i, j, -1, 0
        # 왼쪽으로, 아래로 반사
        if bx == 0 and by == -1:
            return i, j, 1, 0
        # 오른쪽으로, 왼쪽반사
        if bx == 0 and by == 1:
            return i, j, 0, -1

    if shpae == 3:
        # 위로올라감, 왼쪽
        if bx == -1 and by == 0:
            return i, j, 0, -1
        # 아래로, 위로
        if bx == 1 and by == 0:
            return i, j, -1, 0
        # 왼쪽, 오른쪽
        if bx == 0 and by == -1:
            return i, j, 0, 1
        # 오른쪽, 아래
        if bx == 0 and by == 1:
            return i, j, 1, 0

    if shpae == 4:
        # 위로, 아래로
        if bx == -1 and by == 0:
            return i, j, 1, 0
        # 아래로, 왼쪽
        if bx == 1 and by == 0:
            return i, j, 0, -1
        # 왼쪽, 오른쪽
        if bx == 0 and by == -1:
            return i, j, 0, 1
        # 오른쪽 위쪽
        if bx == 0 and by == 1:
            return i, j, -1, 0

    if shpae == 5:
        # 아래로 반사
        if bx == -1 and by == 0:
            return i, j, 1, 0
        # 위로 반사
        if bx == 1 and by == 0:
            return i, j, -1, 0
        # 오른쪽으로 반사
        if bx == 0 and by == -1:
            return i, j, 0, 1
        # 왼쪽으로 반사
        if bx == 0 and by == 1:
            return i, j, 0, -1
        pass
    pass


def start(i, j, bx, by, count):
    # print('+', i, j, bx, by, count)
    global cnt, sx, sy, blackHole, warmHole, arr

    ni, nj = i + bx, j + by

    # 다음 점이 시작점이거나 블랙홀이면 return
    if (ni, nj) == (sx, sy):
        cnt = max(cnt, count)
        return

    # 밖
    elif ni < 0 or ni >= N or nj < 0 or nj >= N:
        start(ni, nj, -bx, -by, count + 1)


    elif arr[ni][nj] == 0:
        start(ni, nj, bx, by, count)

    # 벽
    elif arr[ni][nj] > 0 and arr[ni][nj] <= 5:
        ni, nj, bx, by = find(arr[ni][nj], ni, nj, bx, by)
        start(ni, nj, bx, by, count + 1)

    # 웜홀
    elif arr[ni][nj] > 5 and arr[ni][nj] <= 10:
        for w in warmHole[arr[ni][nj]]:
            if w != (ni, nj):
                start(w[0], w[1], bx, by, count)
                break

    # 블랙홀
    elif arr[ni][nj] == -1:
        cnt = max(cnt, count)
        return


for test_case in range(1, T + 1):
    N = int(input())
    sx, sy = 0, 0

    blackHole.clear()
    warmHole.clear()
    arr.clear()
    cnt = 0

    for i in range(N):
        line = list(map(int, input().strip().split(' ')))
        for j in range(N):
            if line[j] == -1:
                blackHole.append((i, j))

            if line[j] > 5 and line[j] <= 10:
                if line[j] in warmHole:
                    warmHole[line[j]].append((i, j))
                else:
                    warmHole[line[j]] = [(i, j)]
        arr.append(line)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                sx, sy = i, j
                for z in range(4):
                    # print('start', i, j, dx[z], dy[z], 0)
                    start(i, j, dx[z], dy[z], 0)

    print('#' + str(test_case), cnt)

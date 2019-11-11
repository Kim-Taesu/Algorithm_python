import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split(' '))

arr = []

r = (-1, -1)
b = (-1, -1)
o = (-1, -1)

for i in range(N):
    line = list(input().strip())

    if 'R' in line: r = (i, line.index('R'))
    if 'B' in line: b = (i, line.index('B'))
    if 'O' in line: o = (i, line.index('O'))
    arr.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

queue.append((r, b, 0))

visit = [(r, b)]

check = False

while queue:
    # print(queue)
    cr, cb, cnt = queue.popleft()

    crx, cry = cr
    cbx, cby = cb

    # 방향 설정
    for d in range(4):
        gx, gy = dx[d], dy[d]

        checkR = False
        checkB = False

        # R
        rnx, rny = crx, cry
        # 특정 방향으로 끝까지 이동
        moveR = 0
        while True:
            if arr[rnx][rny] == '#':
                rnx, rny = rnx - gx, rny - gy
                break
            if arr[rnx][rny] == 'O':
                checkR = True
                break

            moveR += 1
            rnx, rny = rnx + gx, rny + gy

        # B
        bnx, bny = cbx, cby
        # 특정 방향으로 끝까지 이동
        moveB = 0
        while True:
            if arr[bnx][bny] == '#':
                bnx, bny = bnx - gx, bny - gy
                break
            if arr[bnx][bny] == 'O':
                checkB = True
                break

            moveB += 1
            bnx, bny = bnx + gx, bny + gy

        # 구멍에 빠짐

        # B만 빠짐
        if checkB:
            continue

        # R만 빠짐 : 성공 케이스
        elif checkR and not checkB:
            print(cnt + 1)
            queue.clear()
            check = True
            break

        # 비교

        # 두 공 위치가 같을 때
        if rnx == bnx and rny == bny:
            # R이 더 먼저 도착
            if moveR < moveB:
                bnx, bny = bnx - gx, bny - gy
            # B이 더 먼저 도착
            else:
                rnx, rny = rnx - gx, rny - gy

        # 처음 위치랑 비교
        if rnx == crx and rny == cry and bnx == cbx and bny == cby: continue

        # 과거에 왔는지 비교
        if ((rnx,rny),(bnx,bny)) in visit:
            continue

        else:
            visit.append(((rnx,rny),(bnx,bny)))

        data = ((rnx, rny), (bnx, bny), cnt + 1)
        if data not in queue: queue.append(data)

if not check:
    print(-1)

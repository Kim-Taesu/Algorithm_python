import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

R, C, M = map(int, input().strip().split())

arr = [[False] * (C + 1) for _ in range(R + 1)]

for _ in range(M):
    r, c, s, d, z = map(int, input().strip().split())
    arr[r][c] = (s, d, z)

result = 0


def printArr():
    for q in range(1, R + 1):
        for w in range(1, C + 1):
            print(arr[q][w], end='\t')
        print()
    print()


# printArr()


def catch(col):
    global result
    for i in range(R + 1):
        if arr[i][col] != False:
            result += arr[i][col][2]
            arr[i][col] = False
            return result


# 가는 방향의 끝까지 이동
# 남은 거리를 R-1로 나눔
# 짝수면 방향 그대로 나머지 플러스
# 홀수면 반대 방향에서 출발, 반대 방향으로 플러스


def moving(tr, tc, ts, td, tz, visit, speed):
    # print(tr, tc, ts, td, tz, speed)
    tsTmp = speed
    if td == 1:
        tsTmp = tsTmp % (2 * R - 2)
        if tr == 1:
            moving(tr, tc, ts, 2, tz, visit, tsTmp)
            return
        else:
            if tr - tsTmp < 1:
                tsTmp -= (tr - 1)
                moving(1, tc, ts, 2, tz, visit, tsTmp)
            else:
                tr -= tsTmp
                if visit[tr][tc] != False:
                    if visit[tr][tc][2] < tz:
                        visit[tr][tc] = (ts, td, tz)
                else:
                    visit[tr][tc] = (ts, td, tz)
    if td == 2:
        tsTmp = tsTmp % (2 * R - 2)
        if tr == R:
            moving(tr, tc, ts, 1, tz, visit, speed)
            return
        else:
            if tr + tsTmp > R:
                tsTmp -= (R - tr)
                moving(R, tc, ts, 1, tz, visit, tsTmp)
            else:
                tr += tsTmp
                if visit[tr][tc] != False:
                    if visit[tr][tc][2] < tz:
                        visit[tr][tc] = (ts, td, tz)
                else:
                    visit[tr][tc] = (ts, td, tz)
    if td == 3:
        tsTmp = tsTmp % (2 * C - 2)
        if tc == C:
            moving(tr, tc, ts, 4, tz, visit, speed)
            return
        else:
            if tc + tsTmp > C:
                tsTmp -= (C - tc)
                moving(tr, C, ts, 4, tz, visit, tsTmp)
            else:
                tc += tsTmp
                if visit[tr][tc] != False:
                    if visit[tr][tc][2] < tz:
                        visit[tr][tc] = (ts, td, tz)
                else:
                    visit[tr][tc] = (ts, td, tz)
    if td == 4:
        tsTmp = tsTmp % (2 * C - 2)
        if tc == 1:
            moving(tr, tc, ts, 3, tz, visit, tsTmp)
            return
        else:
            if tc - tsTmp < 1:
                tsTmp -= (tc - 1)
                moving(tr, 1, ts, 3, tz, visit, tsTmp)
            else:
                tc -= tsTmp
                if visit[tr][tc] != False:
                    if visit[tr][tc][2] < tz:
                        visit[tr][tc] = (ts, td, tz)
                else:
                    visit[tr][tc] = (ts, td, tz)


def moveShark():
    visit = [[False] * (C + 1) for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if arr[i][j] != False:
                ts, td, tz = arr[i][j][0], arr[i][j][1], arr[i][j][2]
                arr[i][j] = False
                moving(i, j, ts, td, tz, visit, ts)
    return visit


for i in range(1, C + 1):
    # print(i)
    catch(i)
    # printArr()
    arr = moveShark()
    # printArr()

print(result)

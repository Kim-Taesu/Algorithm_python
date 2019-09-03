import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

R, C, M = map(int, input().strip().split())

arr = [[False] * (C + 1) for _ in range(R + 1)]

for _ in range(M):
    r, c, s, d, z = map(int, input().strip().split())
    arr[r][c] = (s, d, z, 1)

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


def moving(tr, tc, ts, td, tz, time):

    if td == 1:
        # 벽에 튕겨나옴
        if tr - ts < 1:
            tsTmp = ts

            # 벽까지 이동
            tsTmp -= tr - 1
            # 방향 변경
            td = 2

            # 벽까지 이동 후 남은거리 계산
            tmp1 = tsTmp // (R - 1)
            tmp2 = tsTmp - (R - 1) * tmp1

            # 현재 위치에서 남은 tmp2 거리만큼 이동
            # 방향 그대로
            if tmp1 % 2 == 0:
                # 이동
                tr = 1 + tmp2
                # 이동위치에 다른 상어 있을 때
                if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                    # 지금 이동한 상어가 더 큼
                    if arr[tr][tc][2] < tz:
                        arr[tr][tc] = (ts, td, tz, time + 1)
                    # 원래 있는 상어가 더 큼
                    else:
                        return
                # 이동위치에 다른 상어 없을 때
                else:
                    # 이동할 상어가 있을 때 그 상어부터 이동
                    if arr[tr][tc] != False and arr[tr][tc][3] == time:
                        tts, ttd, ttz, ttt = arr[tr][tc][0], arr[tr][tc][1], arr[tr][tc][2], arr[tr][tc][3]
                        arr[tr][tc] = False
                        moving(tr, tc, tts, ttd, ttz, ttt)
                    arr[tr][tc] = (ts, td, tz, time + 1)

            # 반대 위치에서 남은 tmp2 거리만큼 이동
            # 방향 변경
            else:
                td = 1
                # 이동
                tr = R - tmp2
                # 이동위치에 다른 상어 있을 때
                if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                    # 지금 이동한 상어가 더 큼
                    if arr[tr][tc][2] < tz:
                        arr[tr][tc] = (ts, td, tz, time + 1)
                    # 원래 있는 상어가 더 큼
                    else:
                        return
                # 이동위치에 다른 상어 없을 때
                else:
                    arr[tr][tc] = (ts, td, tz, time + 1)
            pass

        # 벽까지 가거나 그전에 멈춤
        else:
            # 이동
            tr = tr - ts
            # 이동위치에 다른 상어 있을 때
            if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                # 지금 이동한 상어가 더 큼
                if arr[tr][tc][2] < tz:
                    arr[tr][tc] = (ts, td, tz, time + 1)
                # 원래 있는 상어가 더 큼
                else:
                    return
            # 이동위치에 다른 상어 없을 때
            else:
                # 이동할 상어가 있을 때 그 상어부터 이동
                if arr[tr][tc] != False and arr[tr][tc][3] == time:
                    tts, ttd, ttz, ttt = arr[tr][tc][0], arr[tr][tc][1], arr[tr][tc][2], arr[tr][tc][3]
                    arr[tr][tc] = False
                    moving(tr, tc, tts, ttd, ttz, ttt)
                arr[tr][tc] = (ts, td, tz, time + 1)

            pass
        pass
    elif td == 2:
        # 벽에 튕겨나옴
        if tr + ts > R:
            tsTmp = ts

            # 벽까지 이동
            tsTmp -= R - tr

            # 방향 변경
            td = 1
            # 벽까지 이동 후 남은거리 계산
            tmp1 = tsTmp // (R - 1)
            tmp2 = tsTmp - (R - 1) * tmp1

            # 현재 위치에서 남은 tmp2 거리만큼 이동
            # 방향 그대로
            if tmp1 % 2 == 0:
                # 이동
                tr = R - tmp2
                # 이동위치에 이동한 다른 상어 있을 때
                if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                    # 지금 이동한 상어가 더 큼
                    if arr[tr][tc][2] < tz:
                        arr[tr][tc] = (ts, td, tz, time + 1)
                    # 원래 있는 상어가 더 큼
                    else:
                        return

                # 이동위치에 이동한 다른 상어 없을 때
                else:
                    # 이동할 상어가 있을 때 그 상어부터 이동
                    if arr[tr][tc] != False and arr[tr][tc][3] == time:
                        tts, ttd, ttz, ttt = arr[tr][tc][0], arr[tr][tc][1], arr[tr][tc][2], arr[tr][tc][3]
                        arr[tr][tc] = False
                        moving(tr, tc, tts, ttd, ttz, ttt)
                    arr[tr][tc] = (ts, td, tz, time + 1)

            # 반대 위치에서 남은 tmp2 거리만큼 이동
            # 방향 변경
            else:
                td = 2
                # 이동
                tr = 1 + tmp2
                # 이동위치에 다른 상어 있을 때
                if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                    # 지금 이동한 상어가 더 큼
                    if arr[tr][tc][2] < tz:
                        arr[tr][tc] = (ts, td, tz, time + 1)
                    # 원래 있는 상어가 더 큼
                    else:
                        return
                # 이동위치에 다른 상어 없을 때
                else:
                    arr[tr][tc] = (ts, td, tz, time + 1)
            pass

        # 벽까지 가거나 그전에 멈춤
        else:
            # 이동
            tr = tr + ts
            # 이동위치에 다른 상어 있을 때
            if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                # 지금 이동한 상어가 더 큼
                if arr[tr][tc][2] < tz:
                    arr[tr][tc] = (ts, td, tz, time + 1)
                # 원래 있는 상어가 더 큼
                else:
                    return
            # 이동위치에 다른 상어 없을 때
            else:
                # 이동할 상어가 있을 때 그 상어부터 이동
                if arr[tr][tc] != False and arr[tr][tc][3] == time:
                    tts, ttd, ttz, ttt = arr[tr][tc][0], arr[tr][tc][1], arr[tr][tc][2], arr[tr][tc][3]
                    arr[tr][tc] = False
                    moving(tr, tc, tts, ttd, ttz, ttt)
                arr[tr][tc] = (ts, td, tz, time + 1)

            pass
        pass
    elif td == 3:
        # 벽에 튕겨나옴
        if tc + ts > C:
            tsTmp = ts

            # 벽까지 이동
            tsTmp -= C - tc

            # 방향 변경
            td = 4
            # 벽까지 이동 후 남은거리 계산
            tmp1 = tsTmp // (C - 1)
            tmp2 = tsTmp - (C - 1) * tmp1

            # 현재 위치에서 남은 tmp2 거리만큼 이동
            # 방향 그대로
            if tmp1 % 2 == 0:
                # 이동
                tc = C - tmp2
                # 이동위치에 이동한 다른 상어 있을 때
                if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                    # 지금 이동한 상어가 더 큼
                    if arr[tr][tc][2] < tz:
                        arr[tr][tc] = (ts, td, tz, time + 1)
                    # 원래 있는 상어가 더 큼
                    else:
                        return

                # 이동위치에 이동한 다른 상어 없을 때
                else:
                    # 이동할 상어가 있을 때 그 상어부터 이동
                    if arr[tr][tc] != False and arr[tr][tc][3] == time:
                        tts, ttd, ttz, ttt = arr[tr][tc][0], arr[tr][tc][1], arr[tr][tc][2], arr[tr][tc][3]
                        arr[tr][tc] = False
                        moving(tr, tc, tts, ttd, ttz, ttt)
                    arr[tr][tc] = (ts, td, tz, time + 1)

            # 반대 위치에서 남은 tmp2 거리만큼 이동
            # 방향 변경
            else:
                td = 3
                # 이동
                tc = 1 + tmp2
                # 이동위치에 다른 상어 있을 때
                if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                    # 지금 이동한 상어가 더 큼
                    if arr[tr][tc][2] < tz:
                        arr[tr][tc] = (ts, td, tz, time + 1)
                    # 원래 있는 상어가 더 큼
                    else:
                        return
                # 이동위치에 다른 상어 없을 때
                else:
                    arr[tr][tc] = (ts, td, tz, time + 1)
            pass

        # 벽까지 가거나 그전에 멈춤
        else:
            # 이동
            tc = tc + ts
            # 이동위치에 다른 상어 있을 때
            if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                # 지금 이동한 상어가 더 큼
                if arr[tr][tc][2] < tz:
                    arr[tr][tc] = (ts, td, tz, time + 1)
                # 원래 있는 상어가 더 큼
                else:
                    return
            # 이동위치에 다른 상어 없을 때
            else:
                # 이동할 상어가 있을 때 그 상어부터 이동
                if arr[tr][tc] != False and arr[tr][tc][3] == time:
                    tts, ttd, ttz, ttt = arr[tr][tc][0], arr[tr][tc][1], arr[tr][tc][2], arr[tr][tc][3]
                    arr[tr][tc] = False
                    moving(tr, tc, tts, ttd, ttz, ttt)
                arr[tr][tc] = (ts, td, tz, time + 1)

            pass
        pass
    elif td == 4:
        # 벽에 튕겨나옴
        if tc - ts < 1:
            tsTmp = ts

            # 벽까지 이동
            tsTmp -= tc - 1
            # 방향 변경
            td = 3

            # 벽까지 이동 후 남은거리 계산
            tmp1 = tsTmp // (C - 1)
            tmp2 = tsTmp - (C - 1) * tmp1

            # 현재 위치에서 남은 tmp2 거리만큼 이동
            # 방향 그대로
            if tmp1 % 2 == 0:
                # 이동
                tc = 1 + tmp2
                # 이동위치에 다른 상어 있을 때
                if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                    # 지금 이동한 상어가 더 큼
                    if arr[tr][tc][2] < tz:
                        arr[tr][tc] = (ts, td, tz, time + 1)
                    # 원래 있는 상어가 더 큼
                    else:
                        return
                # 이동위치에 다른 상어 없을 때
                else:
                    # 이동할 상어가 있을 때 그 상어부터 이동
                    if arr[tr][tc] != False and arr[tr][tc][3] == time:
                        tts, ttd, ttz, ttt = arr[tr][tc][0], arr[tr][tc][1], arr[tr][tc][2], arr[tr][tc][3]
                        arr[tr][tc] = False
                        moving(tr, tc, tts, ttd, ttz, ttt)
                    arr[tr][tc] = (ts, td, tz, time + 1)

            # 반대 위치에서 남은 tmp2 거리만큼 이동
            # 방향 변경
            else:
                td = 4
                # 이동
                tc = C - tmp2
                # 이동위치에 다른 상어 있을 때
                if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                    # 지금 이동한 상어가 더 큼
                    if arr[tr][tc][2] < tz:
                        arr[tr][tc] = (ts, td, tz, time + 1)
                    # 원래 있는 상어가 더 큼
                    else:
                        return
                # 이동위치에 다른 상어 없을 때
                else:
                    arr[tr][tc] = (ts, td, tz, time + 1)
            pass

        # 벽까지 가거나 그전에 멈춤
        else:
            # 이동
            tc = tc - ts
            # 이동위치에 다른 상어 있을 때
            if arr[tr][tc] != False and arr[tr][tc][3] == time + 1:
                # 지금 이동한 상어가 더 큼
                if arr[tr][tc][2] < tz:
                    arr[tr][tc] = (ts, td, tz, time + 1)
                # 원래 있는 상어가 더 큼
                else:
                    return
            # 이동위치에 다른 상어 없을 때
            else:
                # 이동할 상어가 있을 때 그 상어부터 이동
                if arr[tr][tc] != False and arr[tr][tc][3] == time:
                    tts,ttd,ttz, ttt = arr[tr][tc][0], arr[tr][tc][1], arr[tr][tc][2], arr[tr][tc][3]
                    arr[tr][tc] = False
                    moving(tr, tc, tts,ttd,ttz,ttt)
                arr[tr][tc] = (ts, td, tz, time + 1)

            pass
        pass

    pass


def moveShark(time):
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if arr[i][j] != False and arr[i][j][3] == time:
                ts, td, tz = arr[i][j][0], arr[i][j][1], arr[i][j][2]
                arr[i][j] = False
                moving(i, j, ts, td, tz, time)
    pass


for i in range(1, C + 1):
    catch(i)
    # printArr()
    moveShark(i)
    # printArr()

print(result)

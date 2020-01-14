# sys.setrecursionlimit(10 ** 6)
from copy import deepcopy

T = int(input())

# 0부터 떨어지는거
# 해당 w에 가장 위의 H값 찾고
# 숫자 1이면 스탑
# 숫자 1아니면 연쇄 충돌


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def collide(h, w, size, arrTmp, H, W):
    # print('collide', h, w, size)

    # 4가지 방향
    for z in range(4):
        nx, ny = h, w

        # 벽돌 크기만큼 간다.
        for s in range(size - 1):
            nx += dx[z]
            ny += dy[z]

            # 범위 안에 있고 벽돌이 있으면
            if nx >= 0 and nx < H and ny >= 0 and ny < W and arrTmp[nx][ny] != 0:
                # print('++remove', nx, ny, arrTmp[nx][ny], arr[nx][ny])

                # 연쇄 충돌할 벽돌 값
                sizeTmp = arrTmp[nx][ny]

                # 충돌한 벽돌 제거
                arrTmp[nx][ny] = 0

                # 충돌 벽돌의 값이 1이상이면 또 연쇄 충돌
                if sizeTmp > 1:
                    collide(nx, ny, sizeTmp, arrTmp, H, W)


def drop(result, N, W, H, arr):
    # print('drop', N)

    # 구슬 개수 0
    if N == 0:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0: cnt += 1
                # print(arr[i][j],end=' ')
            # print()
        # print(cnt)
        return cnt

    # 0부터 떨어짐
    for w in range(W):
        arrTmp = deepcopy(arr)

        # 해당 w에 가장 위의 h값 찾기

        size = 0
        isCollide = False
        for h in range(H):
            if arrTmp[h][w] != 0:
                isCollide = True
                # 충돌 벽돌 값 기억
                size = arrTmp[h][w]

                # 충돌했으니 삭제
                arrTmp[h][w] = 0
                break

        if isCollide:
            # print('+w', w)
            # 연쇄 충돌
            if size > 1:
                collide(h, w, size, arrTmp, H, W)

                # 구슬 정리
                for j in range(W):
                    arrange = []
                    for i in range(H):
                        if arrTmp[i][j] != 0:
                            arrange.append(arrTmp[i][j])
                            arrTmp[i][j] = 0

                    hTmp = H - 1
                    while len(arrange) > 0:
                        arrTmp[hTmp][j] = arrange.pop()
                        hTmp -= 1

            # for a in arrTmp:
            #     print(a)
            # print()

            # 구슬 드롭
            result = min(result, drop(result, N - 1, W, H, arrTmp))
    return result


for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = []
    for i in range(H):
        arr.append(list(map(int, input().strip().split(' '))))
    result = W * H
    answer = drop(result, N, W, H, arr)
    if result == answer: answer = 0
    print('#' + str(test_case), str(answer))

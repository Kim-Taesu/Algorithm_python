import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().strip().split(' '))
r, c, d = map(int, input().strip().split(' '))
visit = [[0] * M for _ in range(N)]
arr = []
for _ in range(N):
    line = list(map(int, input().strip().split(' ')))
    arr.append(line)

# 각 방향에 따른 왼쪽 방향
direction = {
    0: ((0, -1), 3), 1: ((-1, 0), 0), 2: ((0, 1), 1), 3: ((1, 0), 2)
}

back_direction = {
    0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)
}

cleanCount = 0


def cleanUp(r, c, d):
    # print(r, c, d)
    global cleanCount

    # 기저 사례 (벽이면 끝)
    if arr[r][c] == 1: return

    # 현재 위치 청소
    if arr[r][c] == 0:
        arr[r][c] = 2
        cleanCount += 1

    # for a in arr:
    #     print(a)
    # print()

    tmp_d = d
    for i in range(4):
        left_rc, next_d = direction[tmp_d]

        # 바라보는 방향 기준 왼쪽 방향향
        left_r, left_c = left_rc

        # 현재 위치 기준 왼쪽방향의 좌표
        next_r = r + left_r
        next_c = c + left_c

        # 왼쪽 칸이 청소안한 빈칸이면
        if 0 <= next_r < N and 0 <= next_c < M and arr[next_r][next_c] == 0:
            # print("2-a")
            cleanUp(next_r, next_c, next_d)
            # 다시 되돌아 오지 않기 때문에 return
            return

        # 왼쪽 칸이 청소안한 빈칸이 아니면 방향만 회전하고 계속 탐색
        else:
            # print("2-b")
            tmp_d = next_d

    back_r, back_c = back_direction[d]

    # 후진
    if arr[r + back_r][c + back_c] != 1:
        # print('후진')
        cleanUp(r + back_r, c + back_c, d)


cleanUp(r, c, d)

print(cleanCount)

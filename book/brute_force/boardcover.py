# 3
# 3 7
# #.....#
# #.....#
# ##...##
# 3 7
# # .....#
# # .....#
# ##..###
# 8 10
# ##########
# #........#
# #........#
# #........#
# #........#
# #........#
# #........#
# ##########

# shapes = [
#     [(0, 0), (1, 0), (1, 1)],
#     [(0, 0), (0, -1), (1, -1)],
#     [(0, 0), (-1, 0), (-1, -1)],
#     [(0, 0), (0, 1), (-1, 1)],
# ]


# 포인트를 집어서 생각 (한 답을 한 가지 방법으로빡에 생성할 수 없다.) 중복 문제 해결 방법
shapes = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)],
]


def check(arr, x, y, shape, mode):
    err = True

    for s in shape:
        sx, sy = s

        nx, ny = x + sx, y + sy

        if nx < 0 or nx >= len(arr) or ny < 0 or ny >= len(arr[0]):
            err = False

        arr[nx][ny] += mode
        if arr[nx][ny] > 1:
            err = False

    return err


def find(arr):
    # for a in arr:
    #     print(a)
    # print()

    x = y = -1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                x, y = i, j
                break
        if x != -1: break

    # print(x,y)

    # 모든 칸 다 채움
    if x == -1: return 1

    result = 0
    for shape in shapes:
        if check(arr, x, y, shape, 1):
            result += find(arr)
        check(arr, x, y, shape, -1)

    return result


for test_case in range(int(input())):
    H, W = map(int, input().strip().split(' '))

    arr = [[0] * W for _ in range(H)]
    cnt = 0
    for h in range(H):
        line = list(input().strip())
        for w in range(W):
            if line[w] == '#':
                arr[h][w] = 1
            else:
                cnt += 1
                arr[h][w] = 0

    if cnt % 2 != 0:
        print(0)
        continue
    print(find(arr))

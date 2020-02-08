import copy
from itertools import combinations_with_replacement

N = int(input())

arr = []

max_block = 0
# 위 아래 왼 오
d = ["up", "down", "left", "right"]
# 이동방향, 탐색방향, 시작지점
info = {
    "up": [(0, 1), (1, 0), (0, 0)],
    "down": [(0, 1), (-1, 0), (N - 1, 0)],
    "left": [(1, 0), (0, 1), (0, 0)],
    "right": [(1, 0), (0, -1), (0, N - 1)]
}

for _ in range(N):
    arr.append(list(map(int, input().strip().split())))


def is_range(i, j):
    return 0 <= i < N and 0 <= j < N


def get_direction(size, tmp_dir):
    if size == len(tmp_dir):
        # print(tmp_dir)
        tmp = copy.deepcopy(arr)
        for t in tmp_dir:
            # print(t)
            move(tmp, t)
        find(tmp)

    else:
        for dd in d:
            tmp_dir.append(dd)
            get_direction(size, tmp_dir)
            tmp_dir.pop()


def move(tmp, direction):
    # 위 아래 왼 오
    # (-1, 0), (1, 0), (0, -1), (0, 1)

    cx, cy = info[direction][0]
    nx, ny = info[direction][1]
    sx, sy = info[direction][2]

    for _ in range(N):
        tx, ty = sx, sy
        while is_range(tx, ty):
            if tmp[tx][ty] > 0:
                ttx, tty = tx + nx, ty + ny
                while is_range(ttx, tty):
                    if tmp[ttx][tty] > 0:
                        break
                    else:
                        ttx, tty = ttx + nx, tty + ny
                if is_range(ttx, tty) and tmp[tx][ty] == tmp[ttx][tty]:
                    tmp[tx][ty] *= 2
                    tmp[ttx][tty] = 0
                    ttx, tty = ttx + nx, tty + ny
                tx, ty = ttx, tty
            else:
                tx, ty = tx + nx, ty + ny
        sx, sy = sx + cx, sy + cy

    sx, sy = info[direction][2]
    for _ in range(N):
        tx, ty = sx, sy
        tmp_list = []
        while is_range(tx, ty):
            if tmp[tx][ty] > 0:
                tmp_list.append(tmp[tx][ty])
            tmp[tx][ty] = 0
            tx, ty = tx + nx, ty + ny
        tx, ty = sx, sy
        for t in tmp_list:
            tmp[tx][ty] = t
            tx, ty = tx + nx, ty + ny
        sx, sy = sx + cx, sy + cy



def find(tmp):
    global max_block
    for i in range(N):
        for j in range(N):
            if tmp[i][j] != 0 and max_block < tmp[i][j]:
                max_block = tmp[i][j]

for n in range(1, 5 + 1):
    get_direction(n, [])
print(max_block)
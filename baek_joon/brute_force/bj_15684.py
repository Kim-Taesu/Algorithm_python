import sys

# N : 세로선 (열)
# M : 가로선
# H : 가로선 위치의 개수 (행)

N, M, H = map(int, input().strip().split(' '))
min_value = sys.maxsize

arr = [[0] * ((N * 2) - 1) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().strip().split(' '))
    a -= 1
    b *= 2
    b -= 1
    arr[a][b] = 1


def find(cnt):
    # print('선 횟수', cnt)
    # for a in arr:
    #     print(a)
    # print()

    for j in range(0, (N * 2) - 1, 2):
        start = j

        for i in range(H + 1):
            if i == H:
                if start == j:
                    break
                else:
                    return
            if start - 1 >= 0 and arr[i][start - 1] == 1:
                start -= 2
            elif start + 1 < 2 * N - 1 and arr[i][start + 1] == 1:
                start += 2

    global min_value
    min_value = min(min_value, cnt)


def dfs(cx, cy, cnt):
    # 선 넘어서면
    if cx < 0 or cx >= H or cy < 0 or cy >= 2 * N - 1:
        return

    # 선 3개 넘으면 return
    if cnt > 3:
        return

    find(cnt)

    for ni in range(cx, H):
        for nj in range(1, (N * 2) - 1, 2):
            if arr[ni][nj] == 0:
                arr[ni][nj] = 1
                dfs(ni, nj, cnt + 1)
                arr[ni][nj] = 0


if min_value == sys.maxsize:
    dfs(0, 0, 0)

print(min_value if min_value != sys.maxsize else -1)

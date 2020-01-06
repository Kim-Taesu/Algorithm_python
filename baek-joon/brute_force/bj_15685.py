from collections import deque

N = int(input())

direction = {
    0: (0, 1),
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0)
}

max_value=101
arr = [[False] * max_value for _ in range(max_value)]

result = 0
for _ in range(N):
    x, y, d, g = map(int, input().strip().split(' '))
    tmp = [d]

    for i in range(g):
        for j in range(len(tmp)-1,-1,-1):
            tmp.append((tmp[j] + 1) % 4)

    # print(tmp)
    # 초기값 설정
    arr[y][x] = True

    for t in tmp:
        y, x = y + direction[t][0], x + direction[t][1]
        arr[y][x] = True



for i in range(max_value-1):
    for j in range(max_value-1):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            result += 1

print(result)

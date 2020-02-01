T = int(input())


def move(x, y, d):
    if d == 0:
        return x, y
    elif d == 1:
        return x - 1, y
    elif d == 2:
        return x, y + 1
    elif d == 3:
        return x + 1, y
    elif d == 4:
        return x, y - 1
    pass


def find(x, y):
    global arr
    tmp = []
    for a in range(len(arr)):
        if arr[a][x][y] > 0: tmp.append((a, arr[a][x][y]))
    return tmp


for test_case in range(1, T + 1):
    sample = 0

    M, A = map(int, input().strip().split(' '))

    aMove = list(map(int, input().strip().split(' ')))
    bMove = list(map(int, input().strip().split(' ')))
    aMove.insert(0, 0)
    bMove.insert(0, 0)

    arr = []

    for a in range(A):
        tmp = [[0] * 10 for _ in range(10)]
        Y, X, C, P = map(int, input().strip().split(' '))
        X, Y = X - 1, Y - 1
        tmp[X][Y] = P

        for i in range(X - C, X + C + 1):
            for j in range(Y - C, Y + C + 1):
                if (i, j) == (X, Y): continue
                if not (0 <= i < 10 and 0 <= j < 10): continue
                if abs(X - i) + abs(Y - j) <= C:
                    tmp[i][j] = P
        arr.append(tmp)

    ax, ay = 0, 0
    bx, by = 9, 9

    for z in range(len(aMove)):
        ax, ay = move(ax, ay, aMove[z])
        bx, by = move(bx, by, bMove[z])
        aFind = find(ax, ay)
        bFind = find(bx, by)

        # print(ax, ay)
        # print(bx, by)
        # print(aFind, bFind)
        # print()

        if not bFind and aFind:
            tmp2 = 0
            for q in aFind:
                tmp2 = max(tmp2, q[1])
            sample += tmp2

        elif not aFind and bFind:
            tmp2 = 0
            for q in bFind:
                tmp2 = max(tmp2, q[1])
            sample += tmp2

        elif aFind and bFind:
            tmp2 = 0
            for q in aFind:
                for w in bFind:
                    # 같은 지역
                    if q[0] == w[0]:
                        tmp2 = max(tmp2, q[1])
                    # 다른 지역
                    else:
                        tmp2 = max(tmp2, q[1] + w[1])
            sample += tmp2

    print('#%d %d' % (test_case, sample))

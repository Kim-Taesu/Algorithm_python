T = int(input())


# N : 0, S : 1

def move(arr, n, d):
    if d == 1:
        # 뒤에꺼 빼서
        tmp = arr[n].pop()
        # 앞으로
        arr[n].insert(0, tmp)
    elif d == -1:
        tmp = arr[n].pop(0)
        arr[n].append(tmp)


for test_case in range(1, T + 1):
    sample = 0

    K = int(input())

    arr = []
    go = []
    for _ in range(4):
        line = list(map(int, input().strip().split(' ')))
        arr.append(line)

    for _ in range(K):

        moveList = []
        n, d = map(int, input().strip().split(' '))
        # print(n, d)
        n -= 1

        moveList.append((n, d))

        change = [False] * 4
        change[n] = True

        dTmp = d
        # 왼쪽으로 검색
        for z in range(n - 1, -1, -1):
            # 자성이 다르면
            if arr[z + 1][-2] != arr[z][2] and change[z + 1]:
                moveList.append((z, -dTmp))
                dTmp *= -1
                change[z] = True

        dTmp = d
        # 오른쪽으로 검색
        for z in range(n, 3):
            # 자성이 다르면
            if arr[z + 1][-2] != arr[z][2] and change[z]:
                moveList.append((z + 1, -dTmp))
                dTmp *= -1
                change[z + 1] = True

        # print(moveList)
        for m in moveList:
            tn, td = m
            move(arr, tn, td)

        # for a in arr:
        #     print(a)
        # print()

    # 오른쪽으로 검색
    tmp = 1
    for a in range(4):
        if arr[a][0] == 1:
            sample += tmp
        tmp *= 2
    print('#%d %d' % (test_case, sample))

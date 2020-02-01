T = int(input())

for test_case in range(1, T + 1):
    sample = 0

    N, X = map(int, input().strip().split(' '))
    arr = []

    # 가로축 확인
    for _ in range(N):
        line = list(map(int, input().strip().split(' ')))
        isOk = True
        build = [False] * N
        # print(line)
        for l in range(N - 1):
            # print(l)
            # 경사가 낮음
            if line[l] > line[l + 1]:
                if line[l] - 1 != line[l + 1]:
                    isOk = False
                    break
                check = True
                for x in range(l + 1, (l + 1) + X):
                    if x >= N or line[x] != line[l + 1]:
                        check = False
                        break

                if check:
                    for x in range(l + 1, (l + 1) + X):
                        build[x] = True
                    continue
                else:
                    isOk = False
                    break
                pass

            # 경사가 큼
            elif line[l] < line[l + 1]:
                if line[l] + 1 != line[l + 1]:
                    isOk = False
                    break

                check = True
                for x in range(l - (X - 1), l + 1):
                    if x < 0 or line[x] != line[l] or build[x]:
                        check = False
                        break
                if check:
                    l += 1
                else:
                    isOk = False
                    break
                pass
        # print(check)
        if isOk:
            sample += 1
        # print(result)
        arr.append(line)

    for j in range(N):
        line = []
        for i in range(N):
            line.append(arr[i][j])

        isOk = True
        build = [False] * N
        # print(line)
        for l in range(N - 1):
            # 경사가 낮음
            if line[l] > line[l + 1]:
                if line[l] - 1 != line[l + 1]:
                    isOk = False
                    break
                check = True
                for x in range(l + 1, (l + 1) + X):
                    if x >= N or line[x] != line[l + 1]:
                        check = False
                        break

                if check:
                    for x in range(l + 1, (l + 1) + X):
                        build[x] = True
                    continue
                else:
                    isOk = False
                    break
                pass

            # 경사가 큼
            elif line[l] < line[l + 1]:

                if line[l] + 1 != line[l + 1]:
                    isOk = False
                    break

                check = True
                for x in range(l - (X - 1), l + 1):
                    if x < 0 or line[x] != line[l] or build[x]:
                        check = False
                        break
                if check:
                    l += 1
                else:
                    isOk = False
                    break
                pass
        if isOk:
            sample += 1
        # print(result)

    print('#%d %d' % (test_case, sample))

from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    result = 0

    N, M, K = map(int, input().strip().split(' '))

    virus = deque()
    for _ in range(K):
        i, j, c, d = map(int, input().strip().split(' '))
        virus.append((i, j, c, d))

    while M > 0:
        # 1시간 동안 이동하기 위해 길이 설정
        l = len(virus)

        arr = [[[0] * N for _ in range(N)] for _ in range(2)]
        for v in virus:
            arr[0][v[0]][v[1]] = (v[2], v[3])

        compare = {}

        while virus:
            cur = virus.popleft()
            ci, cj, cc, cd = cur
            # print(ci, cj, cc, cd)

            # 바이러스 이동
            if cd == 1:
                ci -= 1
                pass
            elif cd == 2:
                ci += 1
                pass
            elif cd == 3:
                cj -= 1
                pass
            elif cd == 4:
                cj += 1
                pass

            # 약품 지대이면
            if ci == 0 or cj == 0 or ci == N - 1 or cj == N - 1:
                # 절반으로 죽임
                cc = cc // 2

                if cc == 0:
                    # print('++death')
                    continue

                # 방향 반대로
                if cd == 1:
                    cd = 2
                    pass
                elif cd == 2:
                    cd = 1
                    pass
                elif cd == 3:
                    cd = 4
                    pass
                elif cd == 4:
                    cd = 3
                    pass

            # print('+', ci, cj, cc, cd)

            # 빈 자리로 이동
            if arr[1][ci][cj] == 0:
                # print('++empty')
                arr[1][ci][cj] = (cc, cd)
                pass

            # 미생물이 이미 존재한다.
            else:
                if (ci, cj) in compare:
                    compare[(ci, cj)].append((cc, cd))
                else:
                    compare[(ci, cj)] = [(cc, cd), (arr[1][ci][cj][0], arr[1][ci][cj][1])]

                # print('++plus', cc, arr[1][ci][cj][0])
                # 새로 들어온 미생물이 더 크다.
                if arr[1][ci][cj][0] < cc:
                    cc = cc + arr[1][ci][cj][0]
                    # 새로 들어온 미생물이 먹음
                    arr[1][ci][cj] = (cc, cd)
                    pass

                # 기존 미생물이 더 크다.
                else:
                    cc = cc + arr[1][ci][cj][0]
                    # 기존 미생물이 먹음
                    arr[1][ci][cj] = (cc, arr[1][ci][cj][1])
                    pass
                pass

            l -= 1

        # 겹친 미생물들 최신화
        for key in compare:
            winnerC = 0

            tmp = compare[key]
            winnerD = tmp[0][1]
            winnerCc = tmp[0][0]
            for ttmp in tmp:
                winnerC += ttmp[0]

                if ttmp[0] > winnerCc:
                    winnerCc = ttmp[0]
                    winnerD = ttmp[1]

            arr[1][key[0]][key[1]] = (winnerC,winnerD)

            # 바이러스 정보 최신화
        for i in range(N):
            # print(arr[1][i])
            for j in range(N):
                if arr[1][i][j] != 0:
                    virus.append((i, j, arr[1][i][j][0], arr[1][i][j][1]))
        # print()
        M -= 1

    for i in range(N):
        for j in range(N):
            if arr[1][i][j] != 0:
                result += arr[1][i][j][0]

    print('#%d %d' % (test_case, result))

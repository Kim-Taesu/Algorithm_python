
T = int(input().strip())



for test_case in range(1, T + 1):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N, M, K = map(int, input().strip().split(' '))

    arr = []
    exist = {}
    for i in range(N):
        line = input().strip().split(' ')
        for l in range(len(line)):
            if line[l] != '0':
                arr.append((i, l, int(line[l]), int(line[l])))
                exist[(i, l)] = int(line[l])

    time = 0
    while time < K:
        # print('time',time)
        # print(arr)
        sameTime = {}
        l = len(arr)
        delArr = []
        for a in range(l):
            x, y, h, bh = arr[a]

            if bh > 0:
                bh -= 1
                arr[a] = (x, y, h, bh)

            else:
                # 퍼트리기
                if h == exist[(x, y)]:
                    for z in range(4):
                        nx = x + dx[z]
                        ny = y + dy[z]

                        # 비어있지않음
                        if (nx, ny) in exist:
                            # 동시간에 같이 퍼진 세포가 있다.
                            if (nx, ny) in sameTime:
                                # 퍼질 세포가 기존에 있던 것보다 크다.
                                if exist[(x, y)] > sameTime[(nx, ny)]:
                                    sameTime[(nx, ny)] = exist[(x, y)]
                            pass

                        # 비어있음
                        else:
                            exist[(nx, ny)] = exist[(x, y)]
                            sameTime[(nx, ny)] = exist[(x, y)]
                # print('sametime',sameTime)

                # 활성 시간 감소
                h -= 1

                # 죽은 노드 추가
                if h == 0: delArr.append((x, y, 0, 0))
                arr[a] = (x, y, h, bh)

        # 확산 세포 정보 저장
        for s in sameTime.keys():
            sx, sy = s
            arr.append((sx, sy, sameTime[s], sameTime[s]))

        for d in delArr:
            # print('delete',d)
            arr.remove(d)

        time += 1

    print('#%d %d' %(test_case,len(arr)))
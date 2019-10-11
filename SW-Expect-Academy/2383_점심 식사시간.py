T = int(input())

lastPeople = (0, 0)


def go(pNum, cur):
    if len(cur) == pNum:
        tmp=list(map(int, list(cur)))
        cases.append(tmp)
        return
    for i in range(2):
        go(pNum, cur + str(i))


for test_case in range(1, T + 1):
    cases = []

    # print('start',test_case)
    result = 100000

    people = []
    stairs = []
    stairsLen = []

    N = int(input())
    arr = []
    for i in range(N):
        line = list(map(int, input().strip().split(' ')))
        arr.append(line)
        for j in range(N):
            if line[j] == 1:
                people.append((i, j))
            elif line[j] > 1:
                stairs.append((i, j))
                stairsLen.append(line[j])

    go(len(people), '')

    for case in cases:
        # print(case)
        status = []
        tmp = [[], []]

        # 계단과의 거리 구함
        for person in range(len(people)):
            dest = case[person]
            status.append((dest, abs(stairs[dest][0] - people[person][0]) + abs(stairs[dest][1] - people[person][1])))

        # 계단 거리 정렬
        status = sorted(status, key=lambda x: x[1])

        # 시간 1로 초기화
        time = 1

        # 시작
        while status:
            # print('++', status)
            # print('++',time)
            # print('++',tmp)
            # print()



            delS = []

            # 학생 위치 파악
            for s in status:

                # 계단에 도착해있거나 계단에 도착
                if s[1] < time:

                    # 계단에 들어갈 수 있는지 파악
                    if len(tmp[s[0]]) < 3:
                        # 대기열에서 지워야함
                        delS.append(s)

                        # 계단에 추가
                        tmp[s[0]].append(stairsLen[s[0]])

            # 계단에 들어간 학생 지우기
            for d in delS:
                status.remove(d)

            # 계단 내려가기
            for t in tmp:
                delT = []
                for tt in range(len(t)):
                    # 1칸 내려가기
                    t[tt] -= 1
                    # 다 내려감
                    if t[tt] == 0:
                        # 지울 목록에 추가
                        delT.append(t[tt])

                # 다 내려간사람 지움
                for d in delT:
                    t.remove(d)


            time += 1

        # 계단에 있는 사람 다 내려보내기
        while len(tmp[0])>0 or len(tmp[1]):
            # print('++time',time)
            # print('++',tmp)
            # 계단 내려가기
            for t in tmp:
                delT = []
                for tt in range(len(t)):
                    # 1칸 내려가기
                    t[tt] -= 1
                    # 다 내려감
                    if t[tt] == 0:
                        # 지울 목록에 추가
                        delT.append(t[tt])

                # 다 내려간사람 지움
                for d in delT:
                    t.remove(d)
            time+=1

        result=min(result,time)
        # print('time is ',time)

    print('#%d %d' % (test_case, result))

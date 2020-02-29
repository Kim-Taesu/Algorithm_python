import sys

sys.setrecursionlimit(10 ** 6)

arr = [i for i in range(2, 41, 2)]
cross_1 = [13, 16, 19]
cross_2 = [22, 24]
cross_3 = [28, 27, 26]
cross_4 = [25, 30, 35, 40]
dice = list(map(int, input().strip().split(' ')))


# 직진 상 하 좌 우  (0, 1, 2, 3, 4)

# 말 : (위치, 점수, 방향)


def check_location(next_location):
    # 교차로 안에 없다
    if next_location < 100:
        # 1번 교차로 진입
        if (next_location + 1) == 5:
            return 100
        # 2번 교차로 진입 (경우가 1개)
        elif (next_location + 1) == 10:
            return 200
        # 3번 교차로 진입 (경우가 2개)
        elif (next_location + 1) == 15:
            return 300
        # 교차로 없이 도착점 도착
        elif (next_location + 1) == 20:
            return next_location
        else:
            # 도착점 넘어감
            if next_location >= 20:
                return 'finish'
            # 계속 직진, 다음 위치 반환
            return next_location
    # 1번 교차로
    elif 100 <= next_location < 200:
        # 중앙 교차로 전
        if next_location < 104:
            # 해당 위치 반환
            return next_location
        # 중앙 교차로 도착
        elif next_location == 104:
            # 중앙 교차로
            return 400
        # 4번 교차로 진입
        elif next_location > 104:
            # 4번 교차로로 진입
            if next_location == 105:
                return 401
            elif next_location == 106:
                return 402
            elif next_location == 107:
                return 19
            else:
                return 'finish'
    # 2번 교차로
    elif 200 <= next_location < 300:
        # 중앙 교차로 전
        if next_location < 203:
            return next_location
        # 중앙 교차로 도착
        if next_location == 203:
            return 400
        # 4번 교차로 이동
        if next_location > 203:
            if next_location == 204:
                return 401
            elif next_location == 205:
                return 402
            elif next_location == 206:
                return 19
            else:
                return 'finish'

    # 3번 교차로
    elif 300 <= next_location < 400:
        # 중앙 교차로 전
        if next_location < 304:
            # 해당 위치 반환
            return next_location
        # 중앙 교차로 도착
        elif next_location == 304:
            # 중앙 교차로
            return 400
        # 4번 교차로 진입
        elif next_location > 304:
            # 4번 교차로로 진입
            if next_location == 305:
                return 401
            elif next_location == 306:
                return 402
            elif next_location == 307:
                return 19
            else:
                return 'finish'
    # 4번 교차로
    elif 400 <= next_location < 500:
        # 도착지점이거나 전
        if next_location < 403:
            return next_location
        elif next_location == 403:
            return 19
        else:
            return 'finish'


def is_exist(player, player_num, player_location):
    for i in range(1, 4 + 1):
        # 자기 자신은 검사할 필요가 없다.
        if i == player_num:
            continue
        if player[i][0] == player_location:
            return True
    return False


def get_score(next_location):
    if next_location < 100:
        return arr[next_location]
    elif 100 <= next_location < 200:
        if next_location == 100:
            return arr[4]
        else:
            return cross_1[next_location - 101]
    elif 200 <= next_location < 300:
        if next_location == 200:
            return arr[9]
        else:
            return cross_2[next_location - 201]
    elif 300 <= next_location < 400:
        if next_location == 300:
            return arr[14]
        else:
            return cross_3[next_location - 301]
    elif 400 <= next_location:
        return cross_4[next_location - 400]


max_value = -1


def go(move_list):
    player = {
        1: (-1, 0),
        2: (-1, 0),
        3: (-1, 0),
        4: (-1, 0)
    }
    flag = False
    if move_list == [1, 1, 1, 2, 3, 3, 3, 3, 3, 1]:
        flag = True

    for index, player_num in enumerate(move_list):
        dice_num = dice[index]
        player_location, player_score = player[player_num]

        # 해당 말이 이미 도착했다면 도착에서 이동을 마친다.
        if player_location == 'finish':
            continue

        # 출발 안했으면
        if player_location == -1:
            # 이동 위치, 시작 위치가 0 이므로 1을 뺀다.
            next_location = player_location + dice_num
            # 이동 위치 및 방향 체크
            next_location = check_location(next_location)

            # 이동할 위치에 말이 있다. 케이스 실패 종료
            if is_exist(player, player_num, next_location):
                return

            # 이동함
            next_score = get_score(next_location)
            player[player_num] = (next_location, next_score)

        # 이미 출발했음
        else:

            # 이동 위치
            next_location = player_location + dice_num
            # 이동 위치 및 방향 체크
            next_location = check_location(next_location)

            # print(player_location, dice_num, next_location)

            if next_location == 'finish':
                player[player_num] = (next_location, player_score)
                continue

            # 이동할 위치에 말 있는지 체크
            if is_exist(player, player_num, next_location):
                return

            # 점수 누적 합산
            next_score = get_score(next_location)

            # 다음 위치, 점수 합산, 방향 갱신
            player[player_num] = (next_location, player_score + next_score)

    total_score = 0
    for p in player:
        total_score += player[p][1]
    global max_value
    max_value = max(max_value, total_score)
    return


def dfs(tmp):
    if len(tmp) == 10:
        go(tmp)
        return

    for i in range(1, 4 + 1):
        tmp.append(i)
        dfs(tmp)
        tmp.pop()


for i in range(1, 4 + 1):
    dfs([i])
print(max_value)

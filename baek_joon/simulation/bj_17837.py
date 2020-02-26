import sys

N, K = map(int, input().strip().split(' '))
arr = [[0] * N for _ in range(N)]

red = {}
blue = {}

for i in range(N):
    line = list(map(int, input().strip().split(' ')))
    for j in range(N):
        arr[i][j] = line[j]
        if line[j] == 1:
            if i in red:
                red[i].append(j)
            else:
                red[i] = [j]
        elif line[j] == 2:
            if i in blue:
                blue[i].append(j)
            else:
                blue[i] = [j]
horse = {}
horse_info = {}
direction = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

dir_reverse = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

for index in range(K):
    i, j, k = map(int, input().strip().split(' '))
    i, j = i - 1, j - 1
    # 겹침 유무 확인 (번호, 방향)
    horse[(i, j)] = [index + 1]
    # 1번부터 이동하기 위해 (x,y,방향)
    horse_info[index + 1] = (i, j, k)

turn = 1


def is_range(hnx, hny):
    return 0 <= hnx < N and 0 <= hny < N


def is_blue(hnx, hny):
    if hnx in blue and hny in blue[hnx]:
        return True
    else:
        return False


def is_red(hnx, hny):
    if hnx in red and hny in red[hnx]:
        return True
    else:
        return False


is_finish = False
while turn <= 1000 and not is_finish:
    # 1번 말부터
    # horse : 겹침 유무 확인 (x,y) = (번호)
    # horse_info : 1번부터 이동하기 위해 번호 = (x,y,방향)

    for hi in range(1, K + 1):
        # 출발전 위치
        hx, hy, hd = horse_info[hi]
        # print(turn, 'horse num', hi, hx, hy, hd)

        # 현재 위치의 말 위치 계산
        cur_key = (hx, hy)
        horse_total = len(horse[cur_key])

        if horse_total >= 4:
            is_finish = True
            break

        cur_index = horse[cur_key].index(hi)

        # 현재 자신의 위에 말이 있는지 확인
        is_solo = horse_total - 1 - cur_index == 0

        # 다음 위치 계산
        hdx, hdy = direction[hd]
        hnx, hny = hx + hdx, hy + hdy

        # 범위 아웃 or 파란색
        if not is_range(hnx, hny) or is_blue(hnx, hny):
            # 다음 위치 갱신
            hd = dir_reverse[hd]
            hdx, hdy = direction[hd]
            hnx, hny = hx + hdx, hy + hdy

            # horse : 겹침 유무 확인 (x,y) = (번호)
            # horse_info : 1번부터 이동하기 위해 번호 = (x,y,방향)
            # 갱신 위치도 파란색이거나 범위 밖이면

            # 위치 갱신
            horse_info[hi] = (hx, hy, hd)
            if not is_range(hnx, hny) or is_blue(hnx, hny):
                continue

        # 흰색과 적색은 이동까지는 같다.
        red_flag = is_red(hnx, hny)
        if arr[hnx][hny] == 0 or red_flag:
            # 이동할 위치에 말이 존재하는지 계산
            next_key = (hnx, hny)
            next_exist = next_key in horse

            # 혼자만 움직임
            if is_solo:
                # 자신만 뽑아냄
                tmp = horse[cur_key].pop()
                move_tmp = [tmp]
                # 위치 갱신
                horse_info[tmp] = (hnx, hny, hd)

                # 기존 위치에 말이 전부 이동하면
                if len(horse[cur_key]) == 0:
                    del horse[cur_key]
                # 이동 위치에 말 존재
                if next_exist:
                    horse[next_key].extend(move_tmp)
                    pass
                # 이동 위치에 말 존재하지 않음
                else:
                    horse[next_key] = move_tmp
            else:
                # 자신과 위에 말까지 뽑아냄 (역순 저장)
                move_tmp = []
                for _ in range(cur_index, horse_total):
                    tmp = horse[cur_key].pop()
                    move_tmp.append(tmp)
                    # 위치 갱신
                    horse_info[tmp] = (hnx, hny, horse_info[tmp][2])

                # 하얀색이면 올바른 순서로 정렬
                if not red_flag:
                    move_tmp.reverse()

                # 기존 위치에 말이 전부 이동하면
                if len(horse[cur_key]) == 0:
                    del horse[cur_key]

                # 이동 위치에 말 존재
                if next_exist:
                    # 이동 위치에 저장
                    horse[next_key].extend(move_tmp)
                # 이동 위치에 말 존재하지 않음
                else:
                    horse[next_key] = move_tmp

            if len(horse[next_key]) >= 4:
                is_finish = True
                break
        # print('horse_info', horse_info)
        # print('horse', horse, end='\n\n')

    if not is_finish:
        turn += 1

print(turn if turn <= 1000 else -1)

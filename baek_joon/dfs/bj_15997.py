nations = input().strip().split(' ')
score, result = {}, {}
for n in nations:
    score[n] = 0
    result[n] = 0
predict = []
for _ in range(6):
    line = input().strip().split(' ')
    predict.append(line)


def dfs(game, prob):
    if game == 6:
        score_tmp = []
        for s in score.keys():
            score_tmp.append((s, score[s]))
        score_tmp.sort(key=lambda x: x[1], reverse=True)

        n1, n2, n3, n4 = score_tmp[0][0], score_tmp[1][0], score_tmp[2][0], score_tmp[3][0]
        n1_score, n2_score, n3_score, n4_score = score_tmp[0][1], score_tmp[1][1], score_tmp[2][1], score_tmp[3][1]

        # 개별 1등 2등만 존재 (1등 2등 무조건 진출)
        if n2_score != n3_score:
            result[n1] += prob
            result[n2] += prob
        # 모두 공동 1등 (4팀중 2팀만)
        elif n1_score == n2_score == n3_score == n4_score:
            result[n1] += prob * (2 / 4)
            result[n2] += prob * (2 / 4)
            result[n3] += prob * (2 / 4)
            result[n4] += prob * (2 / 4)
        # 1~3등 까지 공동 1등 (3팀중 2팀만)
        elif n1_score == n2_score:
            result[n1] += prob * (2 / 3)
            result[n2] += prob * (2 / 3)
            result[n3] += prob * (2 / 3)
        # 2~4등 까지 공동 2등 (3팀중 1팀만, 1등은 무조건)
        elif n3_score == n4_score:
            result[n1] += prob
            result[n2] += prob * (1 / 3)
            result[n3] += prob * (1 / 3)
            result[n4] += prob * (1 / 3)
        # 2~3등 까지 공동 2등 (2팀중 1팀만)
        else:
            result[n1] += prob
            result[n2] += prob * (1 / 2)
            result[n3] += prob * (1 / 2)
        return

    a, b = predict[game][:2]
    win, draw, lose = map(float, predict[game][2:])

    score[a] += 3
    dfs(game + 1, prob * win)
    score[a] -= 3

    score[a] += 1
    score[b] += 1
    dfs(game + 1, prob * draw)
    score[a] -= 1
    score[b] -= 1

    score[b] += 3
    dfs(game + 1, prob * lose)
    score[b] -= 3


dfs(0, 1.0)
for n in nations:
    print(result[n])

import sys

input = sys.stdin.readline


def solution(N, stages):
    answer = []
    l = len(stages)
    total = [0 for _ in range(N + 2)]
    fail = [0 for _ in range(N + 2)]
    fail2 = {}

    # 스테이지 별 실패율
    for s in stages:
        fail[s] += 1

    total[1] = l
    for t in range(2, len(total)):
        total[t] = total[t - 1] - fail[t - 1]

    print(total[1:])
    print(fail[1:])

    for f in range(1, len(fail) - 1):

        if total[f] == 0:
            rate = 0.0
        else:
            rate = fail[f] / total[f]

        if rate in fail2:
            fail2[rate].append(f)

        else:
            fail2[rate] = [f]

    key = sorted(list(fail2.keys()), reverse=True)
    print(fail2, key)
    for k in key:
        tmp = sorted(fail2[k])
        for t in tmp:
            answer.append(t)

    return answer

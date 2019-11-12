# 3
# 2 1
# 0 1
# 4 6
# 0 1 1 2 2 3 3 0 0 2 1 3
# 6 10
# 0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5


def find(visit):
    global n, m, friends
    firstFree = -1

    # 제일 빠른 번호
    for i in range(n):
        if not visit[i]:
            firstFree = i
            break

    # 다 찾았을 경우
    if firstFree == -1: return 1

    ret = 0

    # 제일 빠른 번호의 친구 탐색
    for pairWith in range(firstFree + 1, n):
        # 짝이 없고 제일 빠른 번호와 친구일 때
        if not visit[pairWith] and friends[firstFree][pairWith]:
            # 친구 관계 설정
            visit[firstFree] = visit[pairWith] = True
            # 재귀
            ret += find(visit)
            # 친구 관계 해제
            visit[firstFree] = visit[pairWith] = False

    return ret


for test_case in range(int(input())):
    n, m = map(int, input().strip().split(' '))
    line = list(map(int, input().strip().split(' ')))
    friends = [[False] * n for _ in range(n)]

    visit = [False] * n

    minValue = n + 1

    for l in range(0, len(line), 2):

        if line[l] < line[l + 1]:
            minValue = min(minValue, line[l])
        else:
            minValue = min(minValue, line[l + 1])

        friends[line[l]][line[l + 1]] = True
        friends[line[l + 1]][line[l]] = True

    print(find(visit))
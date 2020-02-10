import sys

N = int(input())
N_list = set([i for i in range(N)])
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip().split(' '))))

min_value = sys.maxsize


def get_score(start_team, link_team):
    start_score, link_score = 0, 0
    for si in range(len(start_team) - 1):
        for sj in range(si + 1, len(start_team)):
            start_score += arr[start_team[si]][start_team[sj]]
            start_score += arr[start_team[sj]][start_team[si]]
            link_score += arr[link_team[si]][link_team[sj]]
            link_score += arr[link_team[sj]][link_team[si]]
    return abs(start_score - link_score)


def find_team(index, start_team):
    if len(start_team) == (N // 2):
        global min_value
        link_team = N_list - set(start_team)
        # print(start_team, link_team)
        min_value = min(min_value, get_score(start_team, list(link_team)))

    else:
        for member in range(index + 1, N - 1):
            start_team.append(member)
            find_team(member, start_team)
            start_team.pop()


for i in range(N - 1):
    find_team(i, [i])

print(min_value)

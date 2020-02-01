import sys
from itertools import combinations

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip().split(' '))))

sample = sys.maxsize

items = [i for i in range(N)]
for i in range(1, len(items)):
    tmp = list(combinations(items, i))

    for t in tmp:
        start = list(t)
        link = list(set(items) - set(start))
        # print(start,link)

        startScore = 0
        linkScore = 0

        # start 팀 점수
        if len(start) != 1:
            for s1 in range(len(start)):
                for s2 in range(len(start)):
                    startScore += arr[start[s1]][start[s2]]

        # link 팀 점수
        if len(link) != 1:
            for l1 in range(len(link)):
                for l2 in range(len(link)):
                    linkScore += arr[link[l1]][link[l2]]

        # print(startScore, linkScore)
        sample = min(sample, abs(startScore - linkScore))
print(sample)

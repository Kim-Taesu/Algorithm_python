import sys
from itertools import combinations
N, M = map(int, input().strip().split())
house = []
store = []
for i in range(N):
    line = list(map(int, input().strip().split(' ')))
    for j in range(len(line)):
        if 1 == line[j]:
            house.append((i, j))
        if 2 == line[j]:
            line[j] = 0
            store.append((i, j))
result = sys.maxsize
for stores in combinations(store, M):
    min_value = 0
    for h in house:
        hx, hy = h
        min_dist = sys.maxsize
        for t in stores:
            tx, ty = t
            min_dist = min(min_dist, abs(hx - tx) + abs(hy - ty))
        min_value += min_dist
    result = min(result, min_value)
print(result)

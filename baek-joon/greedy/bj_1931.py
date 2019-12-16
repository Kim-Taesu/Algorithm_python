import sys

sys.setrecursionlimit(10 ** 6)
import heapq

input = sys.stdin.readline
N = int(input().strip())
conf = []
for _ in range(N):
    start, end = map(int, input().strip().split())
    conf.append((start, end))
conf = sorted(conf, key=lambda time: time[0])
conf = sorted(conf, key=lambda time: time[1])


def find(conf):
    count = 0
    time = 0
    for i in conf:
        if i[0] >= time:
            time = i[1]
            count += 1
    return count


print(find(conf))

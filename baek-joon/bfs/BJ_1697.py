import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

n, k = map(int, sys.stdin.readline().strip().split(' '))
queue = deque()
queue.append(n)

time = [-1 for i in range(100009)]
time[n] = 0


def isRange(x):
    return x >= 0 and x <= 100000


while (queue and next != k):
    next = queue.popleft()

    new = []
    new.append(next - 1)
    new.append(next + 1)
    new.append(next * 2)

    for i in new:
        if (isRange(i) and time[i] == -1):
            queue.append(i)
            time[i] = time[next] + 1

print(time[k])

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

n, m, v = map(int, sys.stdin.readline().strip().split())

stack = []
queue = deque()
arr = [[0 for i in range(10002)] for i in range(1002)]

vDfs = [0 for i in range(n + 1)]
vBfs = [0 for i in range(n + 1)]

for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    arr[n1][n2] = 1
    arr[n2][n1] = 1


def dfs(v):
    vDfs[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if (arr[v][i] == 1 and vDfs[i] == 0): dfs(i)
    pass


dfs(v)

print()
queue.append(v)
count = 0
while (queue):
    next = queue.popleft()
    if (vBfs[next] == 0): print(next, end=' ')
    vBfs[next] = 1
    for i in range(1, n + 1):
        if (arr[next][i] and vBfs[i] == 0):
            queue.append(i)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

start, end = map(int, input().strip().split())

M = int(input().strip())

rel = {}
arr = [-1] * (N + 1)
visit = [False] * (N + 1)

for _ in range(M):
    p, c = map(int, input().strip().split())
    arr[c] = p
    if not p in rel:
        rel[p] = [c]
    else:
        rel[p].append(c)

# print(rel)
queue = deque()

count = 0
queue.append((start, count))
visit[start] = True

while queue:
    # print(queue)
    now, c = queue.popleft()

    if now == end:
        print(c)
        sys.exit(0)

    # now 자식 추가
    if now in rel:
        for i in rel[now]:
            if not visit[i]:
                queue.append((i, c + 1))
                visit[i] = True

    # now 부모 추가
    if not arr[now] == -1 and not visit[arr[now]]:
        queue.append((arr[now], c + 1))
        visit[arr[now]] = True

print(-1)

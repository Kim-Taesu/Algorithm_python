import sys
from collections import deque

input = sys.stdin.readline

# F : 전체 층수
# G : 목표 층수
# S : 현재 층수
# U : 올라가는 층수
# D : 내려가는 층수
F, S, G, U, D = map(int, input().strip().split())

visit = [False] * (F + 1)

queue = deque()

queue.append((S, 0))

visit[S] = True
while queue:
    now, count = queue.popleft()

    if now == G:
        print(count)
        sys.exit(0)

    if now + U <= F and not visit[now + U]:
        queue.append((now + U, count + 1))
        visit[now + U] = True
    if now - D > 0 and not visit[now - D]:
        queue.append((now - D, count + 1))
        visit[now - D] = True

print('use the stairs')

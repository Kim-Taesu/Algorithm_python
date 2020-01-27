import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    num = int(sys.stdin.readline().strip())
    visit = [0 for i in range(11 + 1)]
    visit[1] = 1
    visit[2] = 2
    visit[3] = 4
    for i in range(4, num + 1):
        visit[i] = visit[i - 1] + visit[i - 2] + visit[i - 3]
    print(visit, visit[num])

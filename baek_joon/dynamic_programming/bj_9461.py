import sys

sys.setrecursionlimit(10 ** 6)

T = int(sys.stdin.readline().strip())
for z in range(T):
    q = int(sys.stdin.readline().strip())
    visit = [0 for i in range(q + 1)]
    visit[0] = 0
    if (q == 1 or q == 2):
        print(1)
        continue

    visit[1] = 1
    visit[2] = 1

    for i in range(3, q + 1):
        visit[i] = visit[i - 3] + visit[i - 2]

    print(visit[q])

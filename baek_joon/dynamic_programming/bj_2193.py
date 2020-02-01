import sys

n = int(sys.stdin.readline().strip())

if (n == 1 or n == 2):
    print(1)

else:
    visit = []
    visit.append(0)
    visit.append(1)
    visit.append(1)
    for i in range(3, n + 1):
        visit.append(visit[i - 1] + visit[i - 2])
        if (i == n):
            print(visit[n])
            break

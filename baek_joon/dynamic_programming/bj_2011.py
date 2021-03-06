import sys

sys.setrecursionlimit(10 ** 6)

mod = 1000000
max = 5000 + 1

line2 = list(map(int, sys.stdin.readline().strip()))

if (len(line2) == 1 and line2[0] == 0):
    print(0)
    exit()

line = [0 for i in range(max)]
visit = [0 for i in range(max)]

for i in range(1, len(line2) + 1):
    line[i] = int(line2[i - 1])

visit[0] = 1

for i in range(1, len(line2) + 1):
    if (line[i] >= 1 and line[i] <= 9):
        visit[i] = (visit[i - 1] + visit[i]) % mod

    print(line)
    print(visit)
    if (i == 1):
        continue

    temp = line[i] + line[i - 1] * 10
    if (10 <= temp and temp <= 26):
        visit[i] = (visit[i - 2] + visit[i]) % mod

print(visit[len(line2)])

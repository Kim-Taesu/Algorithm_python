import sys

n = int(sys.stdin.readline())

line = list(map(int, sys.stdin.readline().strip().split(' ')))
print(line)

visit = [0 for i in range(len(line))]
visit[0] = line[0]

for i in range(1, len(line)):
    visit[i] = line[i]
    if (visit[i] < visit[i - 1] + visit[i]):
        visit[i] = visit[i - 1] + visit[i]

print(visit)
print(max(visit))

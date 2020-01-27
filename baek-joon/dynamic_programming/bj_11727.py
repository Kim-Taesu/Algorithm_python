n = int(input())
visit = [0 for _ in range(1001)]
visit[1] = 1
visit[0] = 1
for i in range(2, n + 1):
    visit[i] = (visit[i - 1] + visit[i - 2] * 2) % 10007
print(visit[n])

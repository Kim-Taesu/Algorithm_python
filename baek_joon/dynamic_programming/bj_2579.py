n = int(input())
arr = [0 for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
for i in range(n):
    arr[i] = int(input())
visit[0] = arr[0]
visit[1] = visit[0] + arr[1]
for i in range(2, n + 1):
    visit[i] = max(arr[i - 1] + visit[i - 3], visit[i - 2]) + arr[i]
print(visit[n - 1])

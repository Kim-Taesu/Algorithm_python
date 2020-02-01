import sys

n = int(sys.stdin.readline().strip())

arr = [0 for i in range(n + 1)]
visit = [0 for i in range(n + 1)]

for i in range(n):
    arr[i + 1] = int(sys.stdin.readline().strip())

if (n == 1):
    print(arr[1])
else:

    visit[1] = arr[1]
    visit[2] = visit[1] + arr[2]

    for i in range(3, n + 1):
        visit[i] = max(visit[i - 2] + arr[i], visit[i - 3] + arr[i - 1] + arr[i], visit[i - 1])

    print(visit[n])

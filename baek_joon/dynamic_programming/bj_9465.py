for _ in range(int(input())):
    n = int(input())
    arr = []
    for j in range(2):
        arr.append(list(map(int, input().strip().split(' '))))
    visit = [[0] * 100000 for _ in range(2)]

    if n == 1:
        print(max(arr[0][0], arr[1][0]))

    else:
        visit[0][0] = arr[0][0]
        visit[1][0] = arr[1][0]

        visit[0][1] = visit[1][0] + arr[0][1]
        visit[1][1] = visit[0][0] + arr[1][1]

        for j in range(2, n):
            visit[0][j] = max(visit[1][j - 1], visit[1][j - 2]) + arr[0][j]
            visit[1][j] = max(visit[0][j - 1], visit[0][j - 2]) + arr[1][j]
        print(max(visit[0][n - 1], visit[1][n - 1]))

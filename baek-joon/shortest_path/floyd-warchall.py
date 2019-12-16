import sys

input = sys.stdin.readline

INF = 987654321

# 노드 개수 입력
V = int(input().strip())

# 간선 개수 입력
E = int(input().strip())

arr = [[INF] * V for _ in range(V)]

for _ in range(E):
    x, y, w = map(int, input().strip().split())
    arr[x - 1][y - 1] = w

for i in arr:
    print(i)
print()

for k in range(V):
    for i in range(V):
        for j in range(V):
            if arr[i][k] != INF and arr[k][j] != INF:
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in arr:
    print(i)

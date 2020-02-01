import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(now, group, arr, check):
    print(now, group, check)
    check[now] = group
    for i in arr[now]:
        if check[i] == 0:
            if dfs(i, -group, arr, check) is False:
                return False
        elif check[i] == check[now]:
            return False
    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v + 1)]
    check = [0] * (v + 1)

    for _ in range(e):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)

    flag = True

    print(arr)
    for i in range(1, v + 1):
        if check[i] == 0:
            if dfs(i, 1, arr, check) is False:
                flag = False
                break
    print("YES" if flag else "NO")

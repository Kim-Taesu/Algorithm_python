import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
arr = ['1', '2', '3']
is_find = False


def check(s):
    length = len(s)
    limit = length // 2
    start = length - 1
    end = length

    for i in range(1, limit + 1):
        if s[start - i:end - i] == s[start:end]: return False
        start -= 1

    return True


def dfs(s):
    if len(s) == N:
        print(s)
        sys.exit(0)
    else:
        for i in arr:
            if (check(s + i)):
                dfs(s + i)
    pass


for i in arr:
    dfs(i)

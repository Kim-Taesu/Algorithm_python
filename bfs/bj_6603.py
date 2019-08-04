import sys


def dfs(line, result):
    # print(line, result)
    if len(result) == 6:
        for q in result:
            print(q,end=' ')
        print()
        return

    l = len(line)
    for i in range(l):
        cur = line.pop(0)
        if (result and cur < result[len(result) - 1]):
            line.append(cur)
            continue
        result.append(cur)
        dfs(line, result)
        line.append(cur)
        result.pop(len(result) - 1)

    pass


while True:
    line = list(map(int, sys.stdin.readline().strip().split()))
    if line[0] == 0:
        break
    line.pop(0)
    line.sort()
    max = 6

    dfs(line, [])
    print()

S = list(input().strip())
info = {}
for s in S:
    if s in info:
        info[s] += 1
    else:
        info[s] = 1

maxLength = 51
arr = [[[[[False] * 3 for _ in range(3)] for _ in range(maxLength)] for _ in range(maxLength)] for _ in
       range(maxLength)]
line = [0] * 51


def dfs(index, a, b, c, p1, p2, remain):
    # print((index, a, b, c, p1, p2, remain))
    # print(line)
    # 종료 조건
    if a + b + c == len(S):
        return True

    # 방문 체크
    if arr[a][b][c][p1][p2]:
        return False
    arr[a][b][c][p1][p2] = True

    # A 출근
    if 'A' in remain:
        line[index] = 'A'
        if dfs(index + 1, a + 1, b, c, 0, p1, remain.replace('A', '', 1)): return True

    # B 출근
    if 'B' in remain and p1 != 1:
        line[index] = 'B'
        if dfs(index + 1, a, b + 1, c, 1, p1, remain.replace('B', '', 1)): return True

    # C 출근
    if 'C' in remain and p1 != 2 and p2 != 2:
        line[index] = 'C'
        if dfs(index + 1, a, b, c + 1, 2, p1, remain.replace('C', '', 1)): return True

    return False


# a, b, c, 전날, 전전날
if dfs(0, 0, 0, 0, 0, 0, ''.join(S)):
    for l in line:
        if l != 0: print(l, end='')

else:
    print(-1)

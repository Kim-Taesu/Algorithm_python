def dfs(pi, li):
    global pattern, line, visit
    print(pi, li, pattern[:pi + 1], line[:li + 1])

    # 메모이제이션 체크
    if visit[pi][li] != -1:
        return visit[pi][li]

    # 메모이제이션 후 기능
    if pi < len(pattern) and li < len(line) and (pattern[pi] == '?' or pattern[pi] == line[li]):
        # 조건 만족하면 재귀
        visit[pi][li] = dfs(pi + 1, li + 1)
        return visit[pi][li]

    # 기저 사례
    # pattern까지 다찾았으면
    if pi == len(pattern):
        if li == len(line):
            visit[pi][li] = 1
        else:
            visit[pi][li] = 0
        return visit[pi][li]

    # '*' 경우 체크
    if pattern[pi] == '*':
        # pi를 1 높인뒤 재귀
        if dfs(pi + 1, li) == 1 or (li < len(line) and dfs(pi, li + 1) == 1):
            visit[pi][li] = 1
            return visit[pi][li]

    visit[pi][li] = 0
    return visit[pi][li]


pattern = input()
W = int(input())
for _ in range(W):
    line = input().strip()
    tmp = max(len(line), len(pattern))
    visit = [[-1] * (tmp + 1) for _ in range(tmp + 1)]
    if dfs(0, 0):
        print(line)

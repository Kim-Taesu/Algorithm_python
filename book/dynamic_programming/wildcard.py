# 3
# he?p
# 3
# help
# heap
# helpp
# *p*
# 3
# help
# papa
# hello
# *bb*
# 1
# babbbc

C = int(input())


def dfs(pi, si):
    global pattern, dp, line
    print(pi, si, pattern[:pi + 1], line[:si + 1])

    # 메모이제이션 확인
    if dp[pi][si]: return dp[pi][si]

    # 기능 구현
    while si < len(line) and pi < len(pattern) and (pattern[pi] == '?' or pattern[pi] == line[si]):
        pi += 1
        si += 1

    # 기저 사례
    if pi == len(pattern):
        dp[pi][si] = si == len(line)
        return dp[pi][si]

    # '*' 경우 체크
    if pattern[pi] == '*':
        for i in range(len(line) + 1 - si):
            if dfs(pi + 1, i + si):
                dp[pi][si] = True
                return dp[pi][si]

    return False


for _ in range(C):
    pattern = input()
    W = int(input())

    for _ in range(W):
        line = input().strip()
        # print('find', line)
        dp = [[False] * (len(line) + 1) for _ in range(len(line) + 1)]
        if (dfs(0, 0)):
            print(line)
        else:
            print(-1)

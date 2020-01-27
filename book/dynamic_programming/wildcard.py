# 3
# he?p
# 3
# help
# heap
# helpp
# *p *
# 3
# help
# papa
# hello
# *bb *
# 1
# babbbc

C = int(input())


def dp(pi, si):
    global pattern, visit, line
    print(pi, si, pattern[:pi + 1], line[:si + 1])

    # 메모이제이션 확인
    if dp[pi][si]: return dp[pi][si]

    # 기능 구현
    # 단어가 같을때 까지 반복 and pattern과 line의 길이까지
    # ? 도 포함
    while si < len(line) \
            and pi < len(pattern) \
            and (pattern[pi] == '?' or pattern[pi] == line[si]):
        pi += 1
        si += 1

    # 기저 사례
    # pattern까지 다찾았으면
    if pi == len(pattern):
        dp[pi][si] = si == len(line)
        return dp[pi][si]

    # '*' 경우 체크
    if pattern[pi] == '*':
        for i in range(len(line) + 1 - si):
            if dp(pi + 1, i + si):
                dp[pi][si] = True
                return dp[pi][si]

    return False


for _ in range(C):
    pattern = input()
    W = int(input())

    for _ in range(W):
        line = input().strip()
        # print('find', line)
        visit = [[False] * (len(line) + 1) for _ in range(len(line) + 1)]
        if dp(0, 0):
            print(line)
        else:
            print(-1)

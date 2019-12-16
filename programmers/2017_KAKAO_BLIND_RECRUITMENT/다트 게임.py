import math


def solution(dartResult):
    answer = 0

    score = ['S', 'D', 'T']
    option = ['*', '#']
    result = []

    line = list(dartResult)
    current = 0
    flag = False
    for l in line:
        if l not in score and l not in option:
            if flag:
                current = 10
            else:
                result.append(current)
                current = int(l)
                flag = True
        if l in score:
            flag = False
            if l == 'D':
                current = math.floor(math.pow(current, 2))
            if l == 'T':
                current = math.floor(math.pow(current, 3))
        if l in option:
            flag = False
            if l == '*':
                l = len(result)
                result[l - 1] *= 2
                current *= 2
            if l == '#':
                current *= (-1)
    result.append(current)
    answer = sum(result)
    return answer

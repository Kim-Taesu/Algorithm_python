# 시간 나눈다.

def solution(lines):
    answer = 0
    arr = []
    for line in lines:
        lineTmp = line.split(' ')
        h, m, s = map(float, lineTmp[1].split(':'))
        t = float(lineTmp[2][:-1])

        finish = h * 3600 + m * 60 + s
        if finish - t < 0:
            start = 0.0
        else:
            start = finish - t + 0.001
        arr.append((round(start, 3), round(finish, 3)))
    arr.sort()
    print(arr)
    result = []
    for a in arr:
        first = round(a[0] + 1 - 0.001, 3)
        last = round(a[1] + 1 - 0.001, 3)

        cntF = 0
        cntL = 0
        for com in arr:
            if a[0] <= com[1] and com[0] <= first: cntF += 1
            if a[1] <= com[1] and com[0] <= last: cntL += 1

        result.append(cntF)
        result.append(cntL)

    answer = max(result)
    print(result)
    return answer
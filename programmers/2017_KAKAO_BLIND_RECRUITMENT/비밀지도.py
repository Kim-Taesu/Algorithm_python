def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        a = arr1[i]
        b = arr2[i]
        tmp = []
        while a > 0:
            tmp.insert(0, a % 2)
            a = (a - (a % 2)) // 2
        if len(tmp) < n:
            d = n - len(tmp)
            for _ in range(d):
                tmp.insert(0, 0)

        tmp2 = []
        while b > 0:
            tmp2.insert(0, b % 2)
            b = (b - (b % 2)) // 2
        if len(tmp2) < n:
            d = n - len(tmp2)
            for _ in range(d):
                tmp2.insert(0, 0)

        tmp3 = ''
        for i in range(n):
            if tmp[i] + tmp2[i] > 0:
                tmp3 += '#'
            else:
                tmp3 += ' '

        answer.append(tmp3)
    return answer

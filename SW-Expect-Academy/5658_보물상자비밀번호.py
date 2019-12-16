T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split(' '))
    line = list(input())
    length = len(line) // 4
    result = []
    for _ in range(length):
        for li in range(0, len(line), length):
            tmp = ''.join(line[li:li + length])
            if tmp not in result:
                result.append(tmp)

        last = line.pop()
        line.insert(0, last)

    for i in range(len(result)):
        result[i] = int(result[i], 16)

    result.sort(reverse=True)
    print('#' + str(test_case), result[K - 1])

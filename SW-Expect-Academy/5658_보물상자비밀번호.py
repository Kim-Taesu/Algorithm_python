T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split(' '))
    line = list(input())
    length = len(line) // 4
    sample = []
    for _ in range(length):
        for li in range(0, len(line), length):
            tmp = ''.join(line[li:li + length])
            if tmp not in sample:
                sample.append(tmp)

        last = line.pop()
        line.insert(0, last)

    for i in range(len(sample)):
        sample[i] = int(sample[i], 16)

    sample.sort(reverse=True)
    print('#' + str(test_case), sample[K - 1])

T = int(input())


def find(house, K):
    global arr, N

    hx, hy = house
    distance = K - 1
    count = 0

    for i in range(N):
        for j in range(N):

            # 해당 지역이 집이 있고 범위 안이면
            if arr[i][j] == 1 and abs(i - hx) + abs(j - hy) <= distance:
                count += 1
    return count


for test_case in range(1, T + 1):
    sample = 0

    N, M = map(int, input().strip().split(' '))

    houses = []

    arr = []
    for i in range(N):
        line = list(map(int, input().strip().split(' ')))
        for j in range(N):
            if line[j] == 1:
                houses.append((i, j))
        arr.append(line)

    K = 1
    cost = 0
    while K - 1 <= abs((N // 2) - 0) + abs((N // 2) - 0):
        cost = K * K + (K - 1) * (K - 1)
        # 집 목록 브루트 포스
        for i in range(N):
            for j in range(N):
                # 범위 안에 있는 집
                inRangeHouse = find((i, j), K)

                # 해당 집에 설치했을 때의 이득
                if inRangeHouse * M - cost >= 0:
                    # print((i, j))
                    # print('+in range', inRangeHouse)
                    sample = max(sample, inRangeHouse)

        K += 1

    print('#%d %d' % (test_case, sample))

from collections import deque

N, M, T = map(int, input().strip().split(' '))
arr = [[]]
for _ in range(N):
    arr.append(list(map(int, input().strip().split(' '))))


def move(xi, direction, count):
    # 4기준으로 나누고
    count %= M

    # 시계
    if direction == 0:
        start = arr[xi][M - count:M]
        end = arr[xi][:M - count]
        start.extend(end)
        arr[xi] = start

    # 반시계
    else:
        start = arr[xi][count:M]
        end = arr[xi][:count]
        start.extend(end)
        arr[xi] = start


def check(arr):
    visit = [[False] * M for _ in range(N + 1)]
    is_near = False
    # 원판
    for xi in range(1, N + 1):
        # print('\t', xi)
        # 원판 안
        for xxi in range(M):
            # 검사 안했고 지워지지 않은 수라면
            if not visit[xi][xxi] and arr[xi][xxi] != -1:
                queue = deque()
                visit[xi][xxi] = True
                queue.append((xi, xxi))
                queue_tmp = []
                # 인접 검사
                while queue:
                    # 원판 숫자, 원판 내부 순서
                    cxi, cxxi = queue.popleft()
                    queue_tmp.append((cxi, cxxi))

                    # 왼쪽
                    cxxi_left = cxxi - 1 if cxxi - 1 >= 0 else M - 1
                    if not visit[cxi][cxxi_left] and arr[cxi][cxxi_left] == arr[cxi][cxxi]:
                        queue.append((cxi, cxxi_left))
                        visit[cxi][cxxi_left] = True
                        pass

                    # 오른쪽
                    cxxi_right = cxxi + 1 if cxxi + 1 < M else 0
                    if not visit[cxi][cxxi_right] and arr[cxi][cxxi_right] == arr[cxi][cxxi]:
                        queue.append((cxi, cxxi_right))
                        visit[cxi][cxxi_right] = True
                        pass

                    # 위
                    cxi_up = cxi + 1 if cxi + 1 <= N else -1
                    if cxi_up != -1 and not visit[cxi_up][cxxi] and arr[cxi_up][cxxi] == arr[cxi][cxxi]:
                        queue.append((cxi_up, cxxi))
                        visit[cxi_up][cxxi] = True

                    # 아래
                    cxi_down = cxi - 1 if cxi - 1 > 0 else -1
                    if cxi_down != -1 and not visit[cxi_down][cxxi] and arr[cxi_down][cxxi] == arr[cxi][cxxi]:
                        queue.append((cxi_down, cxxi))
                        visit[cxi_down][cxxi] = True

                # 인접한 번호가 있으면
                if len(queue_tmp) > 1:
                    # 같은 수를 모두 지운다.
                    for item in queue_tmp:
                        item_xi, item_xxi = item
                        arr[item_xi][item_xxi] = -1
                    # 인접함 체크
                    is_near = True

    # 모든 원판에서 인접한 경우가 없다.
    if not is_near:
        # 원판 평균을 계산
        arr_total = 0
        arr_count = 0
        for xi in range(1, N + 1):
            for xxi in range(M):
                if arr[xi][xxi] != -1:
                    arr_total += arr[xi][xxi]
                    arr_count += 1
        if arr_count > 0:
            arr_avg = arr_total / arr_count

            # 나머지 원판 값 계산
            for xi in range(1, N + 1):
                for xxi in range(M):
                    if arr[xi][xxi] != -1:
                        if arr[xi][xxi] > arr_avg:
                            arr[xi][xxi] -= 1
                        elif arr[xi][xxi] < arr_avg:
                            arr[xi][xxi] += 1
        else:
            return


for _ in range(T):
    x, d, k = map(int, input().strip().split(' '))

    # 번호가 x의 배수인 원판을
    for xi in range(x, N + 1, x):
        # 회전한다.
        move(xi, d, k)
    check(arr)

result = 0
for xi in range(1, N + 1):
    for xxi in range(M):
        if arr[xi][xxi] != -1:
            result += arr[xi][xxi]
print(result)

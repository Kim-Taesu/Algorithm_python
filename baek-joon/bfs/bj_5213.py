import sys

from collections import deque

N = int(input())

arr = [[0] * (N * 2) for i in range(N)]
number = [[0] * (N * 2) for i in range(N)]
visit = [[False] * (N * 2) for i in range(N)]

i, j = 0, 0
num = 1
last = 0
for _ in range(N * N - N // 2):
    ai, bi = map(int, input().strip().split(' '))

    arr[i][j] = ai
    arr[i][j + 1] = bi
    number[i][j] = num
    number[i][j + 1] = num
    j += 2
    num += 1
    last = num
    if i % 2 == 0 and j == N * 2:
        i += 1
        j = 1

    elif i % 2 != 0 and j == (N * 2) - 1:
        i += 1
        j = 0

queue = deque()

queue.append((0, 0, '1'))
queue.append((0, 1, '1'))

lastRow = [i for i in range(last - N, last)]

# print(lastRow)
visit[0][0] = True
visit[0][1] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

resultNum = sys.maxsize
resultStr = ''
resultLevel = 0
finalCheck = False

while queue:
    # print(queue)
    # for v in visit:
    #     print(v)
    # print()
    i, j, line = queue.popleft()

    if i == N - 1 and (j == (N * 2) - 2 or j == (N * 2) - 1):
        tmp = line.split('|')
        print(len(tmp))
        print(' '.join(tmp))
        finalCheck = True
        break

    if resultLevel < number[i][j]:
        resultLevel = number[i][j]
        tmp = line.split('|')
        resultNum = len(tmp)
        resultStr = ' '.join(tmp)

    for z in range(len(dx)):
        ni = i + dx[z]
        nj = j + dy[z]

        # 범위 check
        if ni < 0 or ni >= N or nj < 0 or nj >= N * 2: continue

        # 빈칸 check
        if arr[ni][nj] == 0: continue

        # 두 타일이 다른지 check
        if number[ni][nj] == number[i][j]: continue

        # 두 변의 수가 같은지 check
        if arr[i][j] != arr[ni][nj]: continue

        # 방문했으면 check
        if visit[ni][nj]: continue

        # 방문 체크
        visit[ni][nj] = True
        queue.append((ni, nj, line + '|' + str(number[ni][nj])))

        if number[ni][nj] == number[ni][nj + 1]:
            visit[ni][nj + 1] = True
            queue.append((ni, nj + 1, line + '|' + str(number[ni][nj + 1])))

        elif number[ni][nj] == number[ni][nj - 1]:
            visit[ni][nj - 1] = True
            queue.append((ni, nj - 1, line + '|' + str(number[ni][nj - 1])))

if not finalCheck:
    print(resultNum)
    print(resultStr)

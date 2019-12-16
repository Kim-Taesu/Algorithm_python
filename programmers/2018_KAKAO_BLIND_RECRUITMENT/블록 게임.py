dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(shape, board, visit, num):
    minx = min(shape, key=lambda x: x[0])
    maxx = max(shape, key=lambda x: x[0])
    miny = min(shape, key=lambda x: x[1])
    maxy = max(shape, key=lambda x: x[1])

    start = (minx[0], miny[1])
    end = (maxx[0], maxy[1])

    # print('+',start,end)

    checkNum = {}
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if board[i][j] != num:
                # 위에서부터 체크
                for z in range(i + 1):
                    # 같은 모형이 위에있으면 아래로 못내려옴
                    if board[z][j] == num: return 0
                    # 다른 모형인데 체크함 ==> 안지워 지는것
                    if board[z][j] != 0 and board[z][j] != num and visit[z][j] != 0: return 0
                    # 다른 모형인데 체크 안함 ==> 나중에 체크해야함
                    if board[z][j] != 0 and board[z][j] != num and visit[z][j] == 0:
                        if board[z][j] in checkNum:
                            continue
                        else:
                            checkNum[board[z][j]] = (z, j)

    tmpAnswer = 0
    if len(checkNum) > 0:
        for c in checkNum:
            cx, cy = checkNum[c]
            num2 = board[cx][cy]
            shape2 = [(cx, cy)]
            visit[cx][cy] = 1
            find(cx, cy, board, visit, shape2)
            # print('!!',shape2,num2)
            tmpAnswer += check(shape2, board, visit, num2)
        if tmpAnswer == 0: return 0

    # print('success',num)
    for s in shape:
        x, y = s
        board[x][y] = 0
    return 1 + tmpAnswer


def find(i, j, board, visit, shape):
    l = len(board)
    for z in range(4):
        ni = i + dx[z]
        nj = j + dy[z]
        if ni >= 0 and ni < l and nj >= 0 and nj < l and board[i][j] == board[ni][nj] and visit[ni][nj] == 0:
            visit[ni][nj] = 1
            shape.append((ni, nj))
            find(ni, nj, board, visit, shape)


def solution(board):
    answer = 0

    l = len(board)
    visit = [[0] * l for _ in range(l)]

    for i in range(l):
        for j in range(l):
            if board[i][j] != 0 and visit[i][j] == 0:
                num = board[i][j]
                shape = [(i, j)]
                visit[i][j] = 1
                find(i, j, board, visit, shape)
                # print(shape,num)
                answer += check(shape, board, visit, num)

    return answer

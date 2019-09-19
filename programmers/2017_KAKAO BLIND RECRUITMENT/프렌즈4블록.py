dx = [0, 1, 1]
dy = [1, 0, 1]


def solution(m, n, board):
    answer = 0

    for b in range(len(board)):
        board[b] = list(board[b])
        print(board[b])

    visit = [[0] * n for _ in range(m)]
    while True:
        isVisit = False
        for i in range(m - 1):
            for j in range(n - 1):
                c = board[i][j]
                if c == '-': continue
                flag = True
                for z in range(3):
                    if c != board[i + dx[z]][j + dy[z]]: flag = False
                if flag:
                    isVisit = True
                    visit[i][j] = 1
                    for z in range(3):
                        visit[i + dx[z]][j + dy[z]] = 1

        if not isVisit: break

        for i in range(m):
            for j in range(n):
                if visit[i][j] == 1:
                    visit[i][j] = 0
                    board[i][j] = '-'
                    answer += 1

        for i in range((m - 1), -1, -1):
            for j in range(n):
                if board[i][j] == '-':
                    iTmp = i
                    cnt = 0
                    while iTmp > 0 and board[iTmp][j] == '-':
                        iTmp -= 1
                        cnt += 1
                    for z in range(cnt):
                        if i - z - cnt < 0:
                            iiTmp = i - z
                            while iiTmp > 0:
                                board[iiTmp][j] = '-'
                                iiTmp -= 1
                            break
                        else:
                            board[i - z][j] = board[i - z - cnt][j]
                            board[i - z - cnt][j] = '-'

        # for b in board:
        #     print(b)

    return answer
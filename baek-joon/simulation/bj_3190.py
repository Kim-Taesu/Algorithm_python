from collections import deque

N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]

for _ in range(K):
    row, col = map(int, input().strip().split(' '))
    arr[row - 1][col - 1] = 1

arr[0][0] = 2

move = deque()

move.append((0, 'D'))

L = int(input())
for _ in range(L):
    X, C = input().split(' ')
    move.append((X, C))

timer = 0

snake = deque()
snakeDir = 1
snake.append((0, 0))

turn_info = {
    'L': {
        1: 4,
        2: 1,
        3: 2,
        4: 3
    },
    'D': {
        1: 2,
        2: 3,
        3: 4,
        4: 1
    }
}

go_info = {
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0),
    4: (0, -1)
}

while True:
    # 방향 회전 체크
    if move and timer == int(move[0][0]):
        X, C = move.popleft()
        snakeDir = turn_info[C][snakeDir]

    timer += 1
    # 다음 위치 추론
    mv = go_info[snakeDir]
    nx, ny = snake[-1][0] + mv[0], snake[-1][1] + mv[1]

    # 벽인지 체크
    if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
        break

    # 갈 방향에 자기 몸인지 체크
    if arr[nx][ny] == 2:
        break

    snake.append((nx, ny))

    # 갈 방향에 사과 체크
    if arr[nx][ny] == 1:
        arr[nx][ny] = 2
    else:
        px, py = snake.popleft()
        arr[px][py] = 0
        arr[nx][ny] = 2

print(timer)

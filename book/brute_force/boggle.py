from collections import deque

arr = [
    ['U', 'R', 'L', 'P', 'M'],
    ['X', 'P', 'R', 'E', 'T'],
    ['G', 'I', 'A', 'E', 'T'],
    ['X', 'T', 'N', 'Z', 'Y'],
    ['X', 'O', 'Q', 'R', 'S']
]

words = ['PRETTY', 'GIRL', 'REPEAT', 'URPRETTEAIGXXTONQZRYS']

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]


def bfs(i, j, word):
    # print(i, j, word)
    queue = deque()

    queue.append((i, j, 0))

    check = False

    while queue:
        cx, cy, index = queue.popleft()

        if index == len(word) - 1:
            check = True
            break

        for q in range(len(dx)):
            nx = cx + dx[q]
            ny = cy + dy[q]

            if not (0 <= nx < len(arr) and 0 <= ny < len(arr[0])): continue

            # print('+',nx,ny,arr[nx][ny])
            if arr[nx][ny] == word[index + 1]:
                queue.append((nx, ny, index + 1))

    return check


for word in words:
    print(word)
    flag = False

    for i in range(len(arr)):
        for j in range(len(arr[0])):

            if not flag and arr[i][j] == word[0]:
                flag = bfs(i, j, word)
                if flag: print('find')

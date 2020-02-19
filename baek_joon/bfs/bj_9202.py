from collections import deque

w = int(input())
words = []
for _ in range(w):
    words.append(input().strip())
input()
b = int(input())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]


def bfs(word, i, j):
    queue = deque()
    queue.append((i, j))

    visit = [[False] * 4 for _ in range(4)]
    visit[i][j] = True

    find = []

    while queue:
        cx, cy = queue.popleft()

        find.append((cx, cy))
        print('\t', queue, find)

        if len(find) == len(word):
            return True

        for z in range(len(dx)):
            nx, ny = cx + dx[z], cy + dy[z]

            if 0 <= nx < 4 and 0 <= ny < 4 and not visit[nx][ny]:
                if arr[nx][ny] in word:
                    queue.append((nx, ny))
                    visit[nx][ny] = True
    return False


def get_score(word):
    size = len(word)
    if 1 <= size <= 2:
        return 0
    elif 3 <= size <= 4:
        return 1
    elif size == 5:
        return 2
    elif size == 6:
        return 3
    elif size == 7:
        return 5
    elif size == 8:
        return 11


def get_long_word(long_word, word):
    if len(long_word) < len(word):
        return word
    else:
        return long_word


for z in range(b):
    arr = []

    for _ in range(4):
        arr.append(list(input().strip()))

    max_score = 0
    long_word = ""
    find_count = 0

    for word_str in words:
        word = list(word_str)
        find_word = False
        print('find', word)
        for i in range(4):
            if find_word:
                break
            for j in range(4):
                if find_word:
                    break
                if arr[i][j] in word:
                    word.remove(arr[i][j])
                    find_word = bfs(word, i, j)
                    max_score += get_score(word)
                    long_word = get_long_word(long_word, word)
                    find_count += 1

    print(max_score, long_word, find_count)

    if z < b - 1:
        input()

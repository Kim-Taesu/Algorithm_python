import sys
from collections import deque

input = sys.stdin.readline
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

        word.remove(arr[cx][cy])
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
    elif len(long_word) == len(word):
        for i in range(len(long_word)):
            if long_word[i] > word[i]:
                return word
            elif long_word[i] < word[i]:
                return long_word
    else:
        return long_word


def dfs(cx, cy, index):
    global is_find, max_score, long_word, find_count
    if is_find:
        return

    if index + 1 == len(word):
        # print(word, 'find')
        max_score += get_score(word)
        long_word = get_long_word(long_word, word)
        find_count += 1
        is_find = True
        return

    for z in range(len(dx)):
        nx, ny = cx + dx[z], cy + dy[z]

        if 0 <= nx < 4 and 0 <= ny < 4 and \
                not visit[nx][ny] and \
                arr[nx][ny] == word[index + 1]:
            visit[nx][ny] = True
            dfs(nx, ny, index + 1)
            visit[nx][ny] = False
            pass


for z in range(b):
    arr = []

    for _ in range(4):
        arr.append(list(input().strip()))
    dump = input().strip()

    max_score = 0
    long_word = []
    find_count = 0

    for word_str in words:
        word = list(word_str)
        # print(word)
        is_find = False
        for i in range(4):
            for j in range(4):
                if arr[i][j] == word[0]:
                    if is_find: break
                    visit = [[False] * 4 for _ in range(4)]
                    visit[i][j] = True
                    dfs(i, j, 0)

    print(max_score, ''.join(long_word), find_count)

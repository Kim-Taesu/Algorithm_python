from collections import deque
from itertools import combinations
from sys import stdin

input = stdin.readline

K = int(input().strip())


def check(line):
    if (len(line) == 1): return True

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            # print('compare : ',line[i],line[j], arr[line[i]][line[j]])
            if (arr[line[i]][line[j]] == 1): return False
    return True
    pass


def bfs(num):
    count=1
    comb = list(combinations(num, count))
    queue = deque()
    for i in comb:
        queue.append(i)

    while (queue):
        # print(queue)
        count+=1
        qSize = len(queue)
        while (qSize):

            line2 = list(num)
            qSize -= 1
            tmp = queue.popleft()

            list1 = []
            for i in tmp:
                list1.append(i)
                line2.remove(i)
            if(line2==[]):continue

            if (check(list1) and check(line2)):
                # print('result : ', list1, line2)
                print('YES')
                return

            # print(list1, line2)

        comb = list(combinations(num, count))
        for i in comb:
            queue.append(i)

    print('NO')
    pass


for z in range(K):
    v, e = map(int, input().strip().split())
    arr = [[0 for _ in range(v + 1)] for _ in range(v + 1)]

    for x in range(e):
        x, y = map(int, input().strip().split())
        arr[x][y] = 1
        arr[y][x] = 1
    # for i in arr:
    #     print(i)

    num = []
    for i in range(1, v + 1):
        num.append(i)

    bfs(num)

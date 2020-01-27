N, M = map(int, input().strip().split())

left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)

sight = {
    '1': [
        [up], [down], [left], [right]
    ],
    '2': [
        [left, right], [up, down]
    ],
    '3': [
        [up, right], [right, down], [down, left], [left, up]
    ],
    '4': [
        [left, up, right], [up, right, down], [right, down, left], [down, left, up]
    ],
    '5': [
        [left, right, up, down]
    ]
}

arr = [[0] * M for _ in range(N)]

number = []

for i in range(N):
    line = input().strip().split()

    for j in range(len(line)):
        if line[j] in ['1', '2', '3', '4', '5']:
            number.append((i, j, line[j]))
        arr[i][j] = line[j]

# print(number)

min_cnt = 987654321
total = 0


def go(number_list, tmp, index):
    # print(number_list, tmp, index)
    if index == len(number_list):
        global min_cnt, total
        total += 1

        visit = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                visit[i][j] = arr[i][j]

        for t in tmp:
            print('\t', t)
            cx, cy, cds = t
            for cd in cds:
                nx, ny = cx, cy
                dx, dy = cd
                while True:
                    nx, ny = nx + dx, ny + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        break
                    if visit[nx][ny] in ['0', '#']:
                        visit[nx][ny] = '#'
                    elif visit[nx][ny] in ['1', '2', '3', '4', '5']:
                        continue
                    else:
                        break

        cnt = 0
        for i in range(N):
            print(visit[i])
            for j in range(M):
                if visit[i][j] == '0': cnt += 1
        min_cnt = min(min_cnt, cnt)
        print(min_cnt)

    else:
        x, y, d = number_list[index]
        for n in sight[d]:
            tmp.append((x, y, n))
            go(number_list, tmp, index + 1)
            tmp.pop()


go(number, [], 0)
print(total)
print(min_cnt)

from collections import deque

R, C, T = map(int, input().strip().split(' '))
arr = [[0] * C for i in range(R)]

machine = []
dust = set()

for i in range(R):
    line = list(map(int, input().strip().split(' ')))
    for j in range(C):
        arr[i][j] = line[j]
        if line[j] == -1:
            machine.append((i, j))
        if line[j] > 0:
            dust.add((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

d = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}

while T > 0:
    # 확산
    dust_size = len(dust)
    new_dust = []
    for _ in range(dust_size):
        cx, cy = dust.pop()

        if arr[cx][cy] // 5 == 0:
            continue

        diffusion = []
        for z in range(4):
            nx, ny = cx + dx[z], cy + dy[z]

            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] >= 0:
                diffusion.append((nx, ny))

        if diffusion:
            diffusion_size = len(diffusion)
            next_dust = arr[cx][cy] // 5

            if next_dust == 0:
                pass
            else:
                while diffusion:
                    diffusion_x, diffusion_y = diffusion.pop()
                    new_dust.append((diffusion_x, diffusion_y, next_dust))
                arr[cx][cy] -= next_dust * diffusion_size

    while new_dust:
        new_x, new_y, new_size = new_dust.pop()
        arr[new_x][new_y] += new_size

    # 공기 청정기
    queue = deque()

    queue.append((machine[0][0], machine[0][1] + 1, 4, 'u', arr[machine[0][0]][machine[0][1] + 1]))
    queue.append((machine[1][0], machine[1][1] + 1, 4, 'd', arr[machine[1][0]][machine[1][1] + 1]))
    arr[machine[0][0]][machine[0][1] + 1] = 0
    arr[machine[1][0]][machine[1][1] + 1] = 0

    while queue:
        mx, my, md, mi, m_tmp = queue.popleft()
        mdx, mdy = d[md]
        nx, ny = mx + mdx, my + mdy

        if md == 4 and ny == C:
            if mi == 'u':
                md = 1
                mdx, mdy = d[md]
                nx, ny = mx + mdx, my + mdy
                pass
            elif mi == 'd':
                md = 2
                mdx, mdy = d[md]
                nx, ny = mx + mdx, my + mdy

        if md == 1 and nx == -1:
            md = 3
            mdx, mdy = d[md]
            nx, ny = mx + mdx, my + mdy

        if md == 2 and nx == R:
            md = 3
            mdx, mdy = d[md]
            nx, ny = mx + mdx, my + mdy

        if md == 3 and ny == -1:
            if mi == 'u':
                md = 2
                mdx, mdy = d[md]
                nx, ny = mx + mdx, my + mdy
                pass
            elif mi == 'd':
                md = 1
                mdx, mdy = d[md]
                nx, ny = mx + mdx, my + mdy

        if arr[nx][ny] == -1:
            continue

        m_tmp, arr[nx][ny] = arr[nx][ny], m_tmp
        queue.append((nx, ny, md, mi, m_tmp))

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                dust.add((i, j))

    T -= 1

count = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            count += arr[i][j]

print(count)

from collections import deque

N = int(input())
arr = [[0] * N for _ in range(N)]
shark_x, shark_y, shark_size, shark_level = 0, 0, 2, 0
for i in range(N):
    line = list(map(int, input().strip().split(' ')))
    for j in range(N):
        if line[j] == 9:
            shark_x, shark_y = i, j
        arr[i][j] = line[j]

di = [(-1, 0), (1, 0), (0, -1), (0, 1)]

call_mother = False
time = 0
while not call_mother:
    # for a in arr:
    #     print(a)
    # print()

    # 탐색
    queue = deque()
    queue.append((shark_x, shark_y, 0))

    visit = [[False] * N for _ in range(N)]
    visit[shark_x][shark_y] = True

    fish_list = []
    find_fish_time = 0

    while queue:
        # 상어 위치, 이동 시간
        cx, cy, ct = queue.popleft()

        # 상어 위치에 있는 물고기 크기
        fish_size = arr[cx][cy]

        # 물고기를 발견한 시간보다 큰 시간이면 pass
        if find_fish_time != 0 and ct > find_fish_time:
            continue

        if 0 < fish_size <= 6:
            # 크기가 큰 물고기 만나면 탐색 끝
            if shark_size < fish_size:
                continue

            # 먹을 수 있는 물고기 발견
            # 발견 시점까지는 탐색을 진행해야 한다.
            if shark_size > fish_size:
                # 발견 시간 저장 (전 기록 보다 작거나 같다)
                find_fish_time = ct

                # 발견한 물고기 리스트에 저장
                fish_list.append((cx, cy))

        for z in range(4):
            nx, ny, nt = cx + di[z][0], cy + di[z][1], ct + 1

            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                queue.append((nx, ny, nt))
                visit[nx][ny] = True

    time += find_fish_time

    if fish_list:
        # print(fish_list, shark_size, shark_level)
        min_x, min_y = N, N
        while fish_list:
            fx, fy = fish_list.pop()

            if fx < min_x:
                min_x, min_y = fx, fy
            if fx == min_x:
                if fy < min_y:
                    min_x, min_y = fx, fy
        # 기존 상어 좌표 초기화
        arr[shark_x][shark_y] = 0

        # 물고기 먹음
        arr[min_x][min_y] = 9

        # 상어 좌표 이동
        shark_x, shark_y = min_x, min_y

        # 상어가 물고기 먹음
        shark_level += 1
        # 상어 크기와 같은 물고기 수를 먹으면
        if shark_size == shark_level:
            shark_size += 1
            shark_level = 0


    else:
        call_mother = True

print(time)

from collections import deque

R, C = map(int, input().strip().split())
arr = [[0] * C for _ in range(R)]
mineral = []

for i in range(R):
    line = list(input())
    for j in range(len(line)):
        if line[j] == '*':
            mineral.append((i, j))
        arr[i][j] = line[j]

N = int(input())
sticks = input().strip().split(' ')

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for index, s in enumerate(sticks):

    # 막대 선택
    stick = R - int(s)
    person = index % 2 == 0 and 'left' or 'right'

    # 창 던지고 맞은거 지우기
    mx = stick
    my = 0
    if person == 'left':
        for j in range(C):
            if arr[mx][j] == 'x':
                arr[mx][j] = '.'
                my = j
                break
    else:
        for j in range(C - 1, -1, -1):
            if arr[mx][j] == 'x':
                arr[mx][j] = '.'
                my = j
                break

    visit = [[False] * C for _ in range(R)]

    # 클러스터 체크
    for j in range(C):
        # 방문했거나 얼음이 없는 칸이면 pass
        if visit[R - 1][j] or arr[R - 1][j] == '.': continue

        # 초기 방문 체크
        visit[R - 1][j] = True

        # 연결된 클러스터 체크
        queue = deque()
        queue.append((R - 1, j))

        while queue:
            cx, cy = queue.popleft()
            for d in direction:
                nx, ny = cx + d[0], cy + d[1]

                # 영역 밖이면 pass
                if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
                # 방문했으면 pass
                if visit[nx][ny]: continue
                # 미네랄 아니면 pass
                if arr[nx][ny] != 'x': continue

                visit[nx][ny] = True
                queue.append((nx, ny))

    # 분리된 클러스터 체크
    clusters = deque()
    for i in range(R):
        for j in range(C):
            if not visit[i][j] and arr[i][j] == 'x':
                # 내려갈 클러스터 위치 초기화
                arr[i][j] = '.'
                clusters.append((i, j))

    # 분리된 클러스터 없으면 pass
    if not clusters:
        continue
    # 분리된 클러스터를 떨어뜨린다.
    else:
        # 최대로 떨어질 수 있는 높이 확인
        check = True
        while check:
            for cluster in clusters:
                cluster_x, cluster_y = cluster
                # 정지 위치 확인
                if cluster_x + 1 == R or arr[cluster_x + 1][cluster_y] == 'x':
                    check = False
                    break

            if check:
                for _ in range(len(clusters)):
                    cluster_x, cluster_y = clusters.popleft()
                    clusters.append((cluster_x + 1, cluster_y))

        # 떨어진 위치 마크
        while clusters:
            cluster_x, cluster_y = clusters.popleft()
            arr[cluster_x][cluster_y] = 'x'

for a in arr:
    print(''.join(a))

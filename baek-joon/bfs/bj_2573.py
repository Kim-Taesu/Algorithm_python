import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

arr = []
queue = deque()
for i in range(N):
    line = list(map(int, input().strip().split()))
    for j in range(M):
        if line[j] != 0:
            queue.append((i, j))
    arr.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(i, j, visit):
    cQueue = deque()
    cQueue.append((i, j))
    # 시작 빙산 위치 방문 체크
    visit[i][j] = True

    while cQueue:
        cx, cy = cQueue.popleft()

        # 시작 빙산 위치 주위 검색
        for z in range(4):
            nx = cx + dx[z]
            ny = cy + dy[z]

            # 범위 안넘고 빙산이 있고 방문하지 않았다면
            if nx >= 0 and ny >= 0 and nx < N and ny < M and arr[nx][ny] > 0 and not visit[nx][ny]:
                # cQueue에 추가
                cQueue.append((nx, ny))
                # 빙산 방문 체크
                visit[nx][ny] = True
    pass


year = 0
while queue:
    l = len(queue)

    year += 1

    minusQueue = deque()

    # 빙산 녹이기 검색
    while l > 0:
        cx, cy = queue.popleft()

        mCount = 0
        # 사방 빙산 검색
        for z in range(4):
            nx = cx + dx[z]
            ny = cy + dy[z]
            # 주변이 바다면
            if nx >= 0 and ny >= 0 and nx < N and ny < M and arr[nx][ny] == 0:
                mCount += 1

        minusQueue.append((cx, cy, mCount))

        l -= 1

    # 검색한 빙산을 적용
    while minusQueue:
        cx, cy, c = minusQueue.popleft()

        # 녹는 빙산 크기보다 기존 빙산이 큰 경우
        if arr[cx][cy] <= c:
            arr[cx][cy] = 0

        # 녹는 빙산 크기보다 기존 빙산이 작은 경우
        else:
            arr[cx][cy] -= c
            queue.append((cx, cy))

    # 빙산 덩어리 체크 배열
    visit = [[False] * M for _ in range(N)]

    # 덩어리 개수
    land = 0

    for i in range(N):
        for j in range(M):
            # 빙산이 있고 방문하지 않았던 빙산이면
            if arr[i][j] > 0 and not visit[i][j]:
                # 덩어리 추가 (빙산 줄기)
                land += 1
                # 덩어리 2개 이상이면 year 출력하고 종료
                if land >= 2:
                    print(year)
                    sys.exit(0)
                # 덩어리 찾기
                check(i, j, visit)

print(0)

import sys

n = int(input())


def find(path, visit, length):
    global n, arr

    # 전부 순회 했을 때
    if len(path) == n:
        return length + arr[path[0]][path[-1]]

    ret = sys.maxsize

    # 아직 가보지 않은 곳으로 재귀함수
    for next in range(n):
        if visit[next]: continue

        # 출발지 설정
        here = visit[-1]

        # 도착지 설정
        path.append(next)

        # 방문 체크
        visit[next] = True

        # 재귀
        cand = find(path, visit, length + arr[here][next])

        ret = min(ret, cand)
        visit[next] = False
        path.pop()

    return ret

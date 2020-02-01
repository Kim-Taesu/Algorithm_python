N, L = map(int, input().strip().split(' '))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip().split(' '))))

# 높이가 1차이 인지
# 길이가 L 만큼 있는지
# 경사로가 범위에서 벗어나는지

total = 0


# 가로 체크
def check1(i):
    visit = [False] * N
    for j in range(N - 1):
        # 높이가 1차이
        if arr[i][j + 1] - arr[i][j] == 1:
            # 경사로 L 범위 체크
            if j - (L - 1) < 0: return False

            # 경사로 놓을 수 있는지
            for l in range(L):
                if arr[i][j] != arr[i][j - l]:
                    return False

            # 경사로 놓기 가능
            else:
                for l in range(L):
                    visit[j - l] = True
        elif arr[i][j + 1] - arr[i][j] > 1:
            return False
    # 반대편 기준 체크
    for j in range(N - 1, 0, -1):
        # 높이가 1차이
        if arr[i][j - 1] - arr[i][j] == 1:
            # 경사로 L 범위 체크
            if j + (L - 1) >= N: return False

            # 경사로 놓을 수 있는지
            for l in range(L):
                # visit 체크
                if arr[i][j] != arr[i][j + l] or visit[j + l]:
                    return False
        elif arr[i][j - 1] - arr[i][j] > 1:
            return False
    return True


def check2(j):
    visit = [False] * N
    for i in range(N - 1, 0, -1):
        # 높이가 1차이
        if arr[i - 1][j] - arr[i][j] == 1:
            # 경사로 L 범위 체크
            if i + (L - 1) >= N: return False

            # 경사로 놓을 수 있는지
            for l in range(L):
                if arr[i][j] != arr[i + l][j]:
                    return False

            # 경사로 놓기 가능
            else:
                for l in range(L):
                    visit[i + l] = True

        elif arr[i - 1][j] - arr[i][j] > 1:
            return False
    # 반대편 기준 체크
    for i in range(N - 1):
        # 높이가 1차이
        if arr[i + 1][j] - arr[i][j] == 1:
            # 경사로 L 범위 체크
            if i - (L - 1) < 0: return False

            # 경사로 놓을 수 있는지
            for l in range(L):
                # visit 체크
                if arr[i][j] != arr[i - l][j] or visit[i - l]:
                    return False
        elif arr[i + 1][j] - arr[i][j] > 1:
            return False
    return True


for i in range(N):
    if check1(i):
        # print('find i', i)
        total += 1
    if check2(i):
        # print('find j', i)
        total += 1

print(total)
# 세로 체크

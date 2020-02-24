import sys

N = int(input())
arr = [[0] * N for _ in range(N)]
for i in range(N):
    line = list(map(int, input().strip().split(' ')))
    for j in range(N):
        arr[i][j] = line[j]

min_value = sys.maxsize


def check(j, i, d1, d2):
    if 0 <= (j + d1) < N and 0 <= (i - d1) < N and \
            0 <= (j + d2) < N and 0 <= (i + d2) < N and \
            0 <= (j + d1 + d2) < N and 0 <= (i - d1 + d2) < N and \
            0 <= (j + d2 + d1) < N and 0 <= (i + d2 - d1) < N:
        location = [0] * 5
        location5 = {i: [j]}
        dy, dx = i, j

        # 3번
        location[2] = sum(arr[dy][:dx])

        # 1번
        for d in range(1, d1 + 1):
            dy, dx = dy - 1, dx + 1
            location5[dy] = [dx]
            location[0] += sum(arr[dy][:dx])

        for ddy in range(dy):
            # 1번
            location[0] += sum(arr[ddy][:dx + 1])
            # 2번
            location[1] += sum(arr[ddy][dx + 1:])

        # 2번
        location[1] += sum(arr[dy][dx + 1:])
        for d in range(1, d2 + 1):
            dy, dx = dy + 1, dx + 1
            if dy in location5:
                location5[dy].append(dx)
            else:
                location5[dy] = [dx]
            location[1] += sum(arr[dy][dx + 1:])

        # 4번
        for d in range(1, d1 + 1):
            dy, dx = dy + 1, dx - 1
            if dy in location5:
                location5[dy].append(dx)
            else:
                location5[dy] = [dx]
            location[3] += sum(arr[dy][dx + 1:])

        for ddy in range(dy + 1, N):
            # 4번
            location[3] += sum(arr[ddy][dx:])
            # 3번
            location[2] += sum(arr[ddy][:dx])
        location[2] += sum(arr[dy][:dx])

        # 3번
        for d in range(1, d2):
            dy, dx = dy - 1, dx - 1
            location5[dy].insert(0, dx)
            location[2] += sum(arr[dy][:dx])

        # 5번
        for l5 in location5:
            if len(location5[l5]) == 1:
                location[4] += arr[l5][location5[l5][0]]
            else:
                lx1, lx2 = location5[l5][0], location5[l5][1]
                location[4] += sum(arr[l5][lx1:lx2 + 1])

        location_min = min(location)
        location_max = max(location)
        global min_value
        if min_value > location_max - location_min:
            min_value = min(min_value, location_max - location_min)
    else:
        return


for i in range(N):
    for j in range(N):
        for d1 in range(1, N):
            if i - d1 < 0:
                break
            for d2 in range(1, N):
                if i + d2 >= N:
                    break
                if j + d1 + d2 >= N:
                    break
                check(j, i, d1, d2)

print(min_value)

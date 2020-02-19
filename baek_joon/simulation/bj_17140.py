r, c, k = map(int, input().strip().split(' '))
arr = []
for _ in range(3):
    arr.append(list(map(int, input().strip().split(' '))))

time = 0
c_size = 3
r_size = 3
while True:
    # print(c_size,r_size)
    if r_size >= r and c_size >= c and arr[r - 1][c - 1] == k:
        break

    if r_size >= c_size:
        # print('R 연산', c_size)
        # R 연산
        max_c_size = 0
        for ar in arr:
            r_info = {}
            while ar:
                value = ar.pop()
                if value == 0:
                    continue
                if value in r_info:
                    r_info[value] += 1
                else:
                    r_info[value] = 1
            for info in sorted(r_info.items(), key=lambda x: [x[1], x[0]]):
                num, num_count = info
                ar.extend([num, num_count])
            max_c_size = max(max_c_size, len(ar))

        if max_c_size > 100:
            max_c_size = 100

        for ar in arr:
            ar_len = len(ar)
            if ar_len > 100:
                ar = ar[:100]
            else:
                ar.extend([0] * (max_c_size - ar_len))

        c_size = max_c_size

    elif r_size < c_size:
        # print('C 연산', r_size)
        # C 연산
        c_info_list = []
        max_r_size = r_size
        for j in range(c_size):
            c_info = {}
            for i in range(r_size):
                value = arr[i][j]
                if value == 0:
                    continue
                if value in c_info:
                    c_info[value] += 1
                else:
                    c_info[value] = 1
            max_r_size = max(max_r_size, len(c_info) * 2)
            c_info_list.append(c_info)

        if max_r_size > 100:
            max_r_size = 100

        for i in range(r_size, max_r_size):
            arr.append([0] * c_size)

        for c_index, c_info in enumerate(c_info_list):
            index = 0
            for info in sorted(c_info.items(), key=lambda x: [x[1], x[0]]):
                if index >= 100:
                    break
                num, num_count = info
                arr[index][c_index] = num
                arr[index + 1][c_index] = num_count
                index += 2
            for i in range(index, max_r_size):
                arr[i][c_index] = 0

        r_size = max_r_size

    # for a in arr:
    #     print(a)
    # print()

    time += 1
    if time > 100:
        break

print(time if time <= 100 else -1)

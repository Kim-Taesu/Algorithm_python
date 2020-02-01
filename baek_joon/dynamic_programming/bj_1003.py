# 1 0 1
# 0 1 2

import sys

T = int(sys.stdin.readline())

for i in range(T):
    num = int(sys.stdin.readline())

    if (num == 0):
        print(1, 0)
        continue
    if (num == 1):
        print(0, 1)
        continue

    arr_z = [0 for i in range(num + 1)]
    arr_o = [0 for i in range(num + 1)]

    arr_z[0] = 1
    arr_o[0] = 0

    arr_z[1] = 0
    arr_o[1] = 1

    for i in range(2, num + 1):
        arr_z[i] = arr_z[i - 1] + arr_z[i - 2]
        arr_o[i] = arr_o[i - 1] + arr_o[i - 2]

    print(arr_z[num], arr_o[num])

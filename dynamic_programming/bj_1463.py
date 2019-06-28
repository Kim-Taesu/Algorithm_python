import sys

num = int(sys.stdin.readline())
arr = [0 for i in range(num + 1)]

arr[1] = 0

for i in range(2, num + 1):
    arr[i] = arr[i - 1] + 1
    if (i % 3 == 0 and arr[i] > arr[int(i / 3)] + 1):
        arr[i] = arr[int(i / 3)] + 1
    if (i % 2 == 0 and arr[i] > arr[int(i / 2)] + 1):
        arr[i] = arr[int(i / 2)] + 1

print(arr[num])

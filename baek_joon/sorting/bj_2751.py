import sys

input = sys.stdin.readline

N = int(input().strip())
arr = []
for _ in range(N):
    arr.append(int(input().strip()))


def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        big, small = [], []
        for item in arr:
            if item > pivot:
                big.append(item)
            elif item < pivot:
                small.append(item)
        return quick(small) + [pivot] + quick(big)


for item in quick(arr):
    print(item)

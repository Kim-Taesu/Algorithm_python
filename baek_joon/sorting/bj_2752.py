data = list(map(int, input().strip().split()))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    else:
        pivot = arr[0]
        big = [item for item in arr if item > pivot]
        small = [item for item in arr if item < pivot]
        return quick_sort(small) + [pivot] + quick_sort(big)


data = quick_sort(data)

for d in data:
    print(d, end=' ')
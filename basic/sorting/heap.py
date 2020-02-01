from basic.sorting.config import make_sample

data_list = make_sample(10)
print(data_list)


def heapify(arr, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
        print('\t', arr)
    print()
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        print('\t', arr)
        heapify(arr, 0, i)
        print('\t\t', arr)
    return arr


print(heap_sort(data_list))

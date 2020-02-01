import random
import time

from basic.sorting.config import make_sample

arr = make_sample(10)


def selection(arr):
    for i in range(len(arr) - 1):
        index_min = i
        for j in range(i + 1, len(arr)):
            if arr[index_min] > arr[j]:
                index_min = j
        arr[index_min], arr[i] = arr[i], arr[index_min]
    return arr


def insertion(arr):
    for i in range(len(arr)):
        while 0 < i and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


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


def merge(left, right):
    result = []
    while len(left) > 0 or len(right):
        if len(left) > 0 and len(right):
            if left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    pass


def heapify(arr, i, arr_length):
    large = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < arr_length and arr[left] > arr[large]:
        large = left
    if right < arr_length and arr[right] > arr[large]:
        large = right
    if large != i:
        arr[i], arr[large] = arr[large], arr[i]
        heapify(arr, large, arr_length)


def heap_sort(arr):
    arr_length = len(arr)
    # 힙 만들기
    for i in range(arr_length // 2 - 1, -1, -1):
        heapify(arr, i, arr_length)

    # 최소힙 구하기
    for i in range(arr_length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr


random.shuffle(arr)
print(arr)
start = time.time()
print(selection(arr))
print('\t', time.time() - start)

random.shuffle(arr)
print(arr)
start = time.time()
print(insertion(arr))
print('\t', time.time() - start)

random.shuffle(arr)
print(arr)
start = time.time()
print(bubble(arr))
print('\t', time.time() - start)

random.shuffle(arr)
print(arr)
start = time.time()
print(quick(arr))
print('\t', time.time() - start)

random.shuffle(arr)
print(arr)
start = time.time()
print(merge_sort(arr))
print('\t', time.time() - start)

random.shuffle(arr)
print(arr)
start = time.time()
print(heap_sort(arr))
print('\t', time.time() - start)

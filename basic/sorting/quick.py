from basic.sorting.config import make_sample

data_list = make_sample(10)
print(data_list)


def quick_sort(arr):
    print(arr)
    arr_length = len(arr)
    if arr_length <= 1:
        return arr
    else:
        pivot = arr[0]
        print('\t', 'pivot', pivot)
        greater = [item for item in arr[1:] if item > pivot]
        lesser = [item for item in arr[1:] if item <= pivot]
        print('\t', lesser, pivot, greater)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


print(quick_sort(data_list))

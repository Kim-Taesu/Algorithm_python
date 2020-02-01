from basic.sorting.config import make_sample

data_list = make_sample(10)
print(data_list)
print()


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        index_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j
        arr[index_min], arr[i] = arr[i], arr[index_min]
        print(data_list)


selection_sort(data_list)
print(data_list)

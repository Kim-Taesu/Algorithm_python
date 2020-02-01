from basic.sorting.config import make_sample

data_list = make_sample(10)
print(data_list)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        while 0 < i and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


print(insertion_sort(data_list))

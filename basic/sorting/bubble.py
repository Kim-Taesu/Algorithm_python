from basic.sorting.config import make_sample

data_list = make_sample(10)
print(data_list)


def bubble_sort(collection):
    for i in range(len(collection)):
        for j in range(i):
            if collection[i] < collection[j]:
                collection[i], collection[j] = collection[j], collection[i]


bubble_sort(data_list)
print(data_list)

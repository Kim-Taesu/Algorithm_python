from basic.sorting.config import make_sample

data_list = make_sample(10)
sample = [0 for _ in range(len(data_list))]
print(data_list)


def shell_sort(collection):
    gap = len(collection) // 2
    while gap > 0:
        print('gap is', gap)
        for start in range(gap):
            gap_insertion_sort(collection, start, gap)
        print("After increments of size", gap, "The list is", collection)
        gap = gap // 2


def gap_insertion_sort(collection, start, gap):
    for i in range(start + gap, len(collection), gap):
        print('\t', i, gap)
        cur_value = collection[i]
        pos = i

        while pos >= gap and collection[pos - gap] > cur_value:
            print('\t\t', pos, gap, pos - gap)
            print('\t\tcompare', collection[pos - gap], cur_value)
            collection[pos] = collection[pos - gap]
            pos = pos - gap
        collection[pos] = cur_value
        print('\t', collection)


shell_sort(data_list)
print(data_list)

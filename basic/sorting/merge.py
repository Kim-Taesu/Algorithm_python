from basic.sorting.config import make_sample

data_list = make_sample(10)
sample = [0 for _ in range(len(data_list))]
print(data_list)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
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


def merge_sort(data_sample):
    print(data_sample)
    if len(data_sample) <= 1:
        return data_sample
    mid = len(data_sample) // 2
    left_list = data_sample[:mid]
    right_list = data_sample[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    print('\t', left_list, right_list)
    return merge(left_list, right_list)


print(merge_sort(data_list))

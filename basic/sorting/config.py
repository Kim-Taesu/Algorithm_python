import random


def make_sample(max_num):
    data = [i for i in range(max_num)]
    random.shuffle(data)
    return data

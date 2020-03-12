import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
N = int(input())
P = list(map(int, input().strip().split(' ')))
perfect_p_list = set(permutations([i for i in range(1, N)], N - 1))
min_count = sys.maxsize


def compute_origin_p(p_tmp):
    result = [0] * N
    result[0] = p_tmp[0]
    for t in range(len(p_tmp) - 1):
        result[p_tmp[t]] = p_tmp[t + 1]
    return result


for perfect_p_tmp in perfect_p_list:
    origin_p = compute_origin_p(perfect_p_tmp)
    diff_count = 0
    for index in range(N):
        if origin_p[index] != P[index]:
            diff_count += 1
    min_count = min(min_count, diff_count)
print(min_count)

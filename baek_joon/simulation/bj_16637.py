N = int(input())
arr = list(input().strip())


def calc_op(item_left, op, item_right):
    if op == '+': return item_left + item_right
    if op == '-': return item_left - item_right
    if op == '*': return item_left * item_right


def find(tmp):
    new_arr = []
    for a in arr:
        new_arr.append(a)
    for index in tmp:
        index_l = arr[index - 1]
        index_r = arr[index + 1]
        value = calc_op(int(index_l), arr[index], int(index_r))
        new_arr[index - 1] = 'n'
        if index + 1 < N:
            new_arr[index + 1] = 'n'
        new_arr[index] = value
    new_arr = list(filter(lambda x: x != 'n', new_arr))

    left = int(new_arr[0])
    for i in range(1, len(new_arr), 2):
        left = calc_op(left, new_arr[i], int(new_arr[i + 1]))
    # print(tmp,'\t', new_arr,left)
    return left


import sys

max_value = -sys.maxsize


def dfs(index, tmp):
    # 괄호 안닫힘
    if len(tmp) >= 2 and abs(tmp[-2] - tmp[-1]) == 2:
        return

    if index > N - 1:
        global max_value
        max_value = max(max_value, find(tmp))
        return

    tmp.append(index)
    dfs(index + 2, tmp)
    tmp.pop()
    dfs(index + 2, tmp)


dfs(1, [])
print(max_value)

s, n = input().strip().split()
s = int(s)
row = s + 2
col = 2 * s + 3

n_list = list(n)

shape = {
    '0': (
        [(0, 0 + 1), (col - 1, 0 + 1)],
        [(0 + 1, 0), (0 + 1, row - 1), (col - 1 - s, 0), (col - 1 - s, row - 1)]
    ),
    '1': (
        [],
        [(0 + 1, row - 1), (col - 1 - s, row - 1)]
    ),
    '2': (
        [(0, 0 + 1), (0 + 1 + s, 0 + 1), (col - 1, 0 + 1)],
        [(0 + 1, row - 1), (col - 1 - s, 0)]
    ),
    '3': (
        [(0, 0 + 1), (0 + 1 + s, 0 + 1), (col - 1, 0 + 1)],
        [(0 + 1, row - 1), (col - 1 - s, row - 1)]
    ),
    '4': (
        [(0 + 1 + s, 0 + 1)],
        [(0 + 1, 0), (0 + 1, row - 1), (col - 1 - s, row - 1)]
    ),
    '5': (
        [(0, 0 + 1), (0 + 1 + s, 0 + 1), (col - 1, 0 + 1)],
        [(0 + 1, 0), (col - 1 - s, row - 1)]
    ),
    '6': (
        [(0, 0 + 1), (0 + 1 + s, 0 + 1), (col - 1, 0 + 1)],
        [(0 + 1, 0), (col - 1 - s, row - 1), (col - 1 - s, 0)]
    ),
    '7': (
        [(0, 0 + 1)],
        [(0 + 1, row - 1), (col - 1 - s, row - 1)]
    ),
    '8': (
        [(0, 0 + 1), (0 + 1 + s, 0 + 1), (col - 1, 0 + 1)],
        [(0 + 1, 0), (0 + 1, row - 1), (col - 1 - s, row - 1), (col - 1 - s, 0)]
    ),
    '9': (
        [(0, 0 + 1), (0 + 1 + s, 0 + 1), (col - 1, 0 + 1)],
        [(0 + 1, 0), (0 + 1, row - 1), (col - 1 - s, row - 1)]
    )
}

sample = [[] for _ in range(2 * s + 3)]
for n_value in n_list:
    arr = [[' '] * row for _ in range(col)]
    r_list, c_list = shape[n_value]

    for r in r_list:
        x, y = r
        for index in range(s):
            arr[x][y + index] = '-'
    for c in c_list:
        x, y = c
        for index in range(s):
            arr[x + index][y] = '|'

    for index, a in enumerate(arr):
        sample[index].append(''.join(a) + ' ')

for r in sample:
    print(''.join(r))

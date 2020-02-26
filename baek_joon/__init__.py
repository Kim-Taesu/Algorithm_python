N = int(input())
total = 2 * N - 1
for i in range(1, 2 * N, 2):
    tmp = total - i
    print(' ' * (tmp // 2), end='')
    print('*' * i, end='')
    print(' ' * (tmp // 2))

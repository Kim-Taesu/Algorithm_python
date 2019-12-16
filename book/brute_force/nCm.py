from collections import deque

n = 6
m = 3

N = [i for i in range(1, n + 1)]

if m == 0:
    print("null")
else:
    print('*' * 20)
    print('중복 없는 경우의 수')
    print('*' * 20)
    queue = deque()
    for num in N: queue.append(str(num))

    while queue:
        line = queue.popleft()
        if len(line) == m:
            print(line)
        else:
            for q in range(int(line[-1]) + 1, n + 1):
                queue.append(line + str(q))

    print('*' * 20)
    print('중복 있는 경우의 수')
    print('*' * 20)
    queue = deque()
    for num in N: queue.append(str(num))

    while queue:
        line = queue.popleft()
        if len(line) == m:
            print(line)
        else:
            for q in range(1, n + 1):
                queue.append(line + str(q))

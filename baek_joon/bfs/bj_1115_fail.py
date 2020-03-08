from collections import deque

N = int(input())
arr = list(map(int, input().strip().split(' ')))
min_value = N + 1

queue = deque()
for i in range(1, N):
    queue.append((str(i), 0 if i == arr[0] else 1))

while queue:
    item, diff_count = queue.popleft()

    if len(item) + 1 == N:
        diff_count = diff_count + 1 if arr[int(item[len(item) - 1])] == 0 else diff_count
        print(item, diff_count)
        continue

    for i in range(1, N):
        if str(i) not in item:
            queue.append((item + str(i), diff_count + 1 if arr[len(item)] == i else diff_count))

print(min_value)

import sys

N = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().strip().split()))
remove = int(sys.stdin.readline().strip())

print(N, line, remove)

# [부모 노드][자식 노드 수]
arr = [[0 for i in range(2)] for i in range(N)]

for i in range(len(line)):
    arr[i][0] = line[i]
    if (line[i] == -1): continue
    arr[line[i]][1] += 1

print(arr)


#
def erase(node):
    # print(node)
    parent = arr[node][0]

    # 부모 노드 자식수 -1
    if (arr[node][0] != -1): arr[parent][1] -= 1

    # 노드 삭제
    arr[node][0] = -2

    for j in range(N):
        if (arr[j][0] == node):
            erase(j)


erase(remove)
# print(arr)

sample = 0
for i in range(N):
    if (arr[i][0] != -2 and arr[i][1] == 0): sample += 1

print(sample)

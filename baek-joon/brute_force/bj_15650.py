line = input().split(' ')

n = int(line[0])
m = int(line[1])

original = []
for i in range(n):
    original.append(int(i + 1))

list = []


def go(list, index):
    # print(original, list, index)
    if (len(list) == m):
        for i in range(len(list)):
            print(list[i], end= ' ')
        print()
    else:
        for i in range(index, n):
            list.append(original[i])
            go(list,i+1)
            list.pop()

go(list, 0)

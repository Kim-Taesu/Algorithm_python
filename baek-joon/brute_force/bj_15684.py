line = input().split(' ')
n = int(line[0])
m = int(line[1])
h = int(line[2])

map = [[0 for i in range(n)] for i in range(m)]

for i in map:
    print(i)

for i in range(m):
    line = input().split(' ')
    aTmp = int(line[0]) - 1
    bTmp = int(line[1]) - 1
    map[aTmp][bTmp] = 1
    # map[aTmp][bTmp + 1] = 1

for i in map:
    print(i)

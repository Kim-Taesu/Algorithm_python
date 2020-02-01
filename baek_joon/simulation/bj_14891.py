# N극이 0, S극이 1
# index 2, 6
# 극이 다르면 반대방향으로 회전

arr = []

for i in range(4):
    arr.append(list(input().strip()))

K = int(input().strip())


def move(num, dTmp):
    global arr
    # print(num, dTmp)
    # 시계
    if dTmp == 1:
        tmp = arr[num].pop()
        arr[num].insert(0, tmp)
    # 반시계
    else:
        tmp = arr[num].pop(0)
        arr[num].append(tmp)


for _ in range(K):
    num, d = map(int, input().strip().split(' '))
    num -= 1

    moveList = [(num, d)]

    dTmp = d
    # 왼쪽 체크
    # print('left check')
    for i in range(num, 0, -1):
        # 극이 다르면 회전한다.
        if arr[i][6] != arr[i - 1][2]:
            dTmp *= -1
            moveList.append((i - 1, dTmp))
        # 극이 같으면 회전을 하지 않으니 스탑
        else:
            break

    dTmp = d
    # 오른쪽 체크
    # print('right check')
    for i in range(num, len(arr) - 1):
        # 극이 다르면 회전한다.
        if arr[i][2] != arr[i + 1][6]:
            dTmp *= -1
            moveList.append((i + 1, dTmp))
        # 극이 같으면 회전을 하지 않으니 스탑
        else:
            break
    # print(moveList)
    for m in moveList:
        move(m[0], m[1])

sample = 0
for i in range(4):
    # S극
    if arr[i][0] == '1':
        sample += pow(2, i)
        pass
print(sample)

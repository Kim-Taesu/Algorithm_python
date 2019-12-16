n = int(input())
line = input().split(' ')
num = []
for i in range(len(line)):
    num.append(int(line[i]))

line = input().split(' ')
op = []
total = 0
for i in range(len(line)):
    op.append(int(line[i]))
    total += int(line[i])


def calc(n1, n2, index):
    if (index == 0):
        return n1 + n2
    if (index == 1):
        return n1 - n2
    if (index == 2):
        return n1 * n2
    if (index == 3):
        if (n1 < 0):
            n1 *= -1
            return (n1 // n2) * (-1)
        return n1 // n2


min = 0
max = 0
flag = True


def go(result, op, count):
    if (count == total):
        global flag, min, max
        if (flag):
            min = result
            max = result
            flag = False
            return

        if (result > max): max = result
        if (result < min): min = result
        return

    for i in range(4):
        if (op[i] == 0): continue
        op[i] = op[i] - 1
        n = num.pop(0)

        go(calc(result, n, i), op, count + 1)

        op[i] = op[i] + 1
        num.insert(0, n)


for i in range(4):
    if (op[i] == 0): continue
    n1 = num.pop(0)
    n2 = num.pop(0)
    op[i] = op[i] - 1

    go(calc(n1, n2, i), op, 1)

    op[i] = op[i] + 1
    num.insert(0, n2)
    num.insert(0, n1)

print(max)
print(min)

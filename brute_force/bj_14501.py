n = int(input())

day = []
price = []

for i in range(n):
    line = input().split(' ')
    day.append(int(line[0]))
    price.append(int(line[1]))

max = 0


def go(start, date, money, past):
    print(start, start + date, past, money + past)
    if (start + date >= n):
        global max
        if (start + date == n):
            money += past
        if (max < money): max = money
        print(' !! max is ', max)
        return

    start += date
    money += past
    print('++next : ', start)
    for i in range(start, n):
        go(i, day[i], money, price[i])


for i in range(n):
    go(i, day[i], 0, price[i])

print(max)

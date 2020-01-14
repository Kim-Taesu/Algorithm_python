line_type, *values = input().split()
for value in values:
    print(line_type, end='')
    val = list(value)
    for index in range(len(val) - 2, -1, -1):
        if val[index] == ']':
            print('[]', end='')
        elif val[index] == '[':
            continue
        elif val[index] in '&*':
            print(val[index], end='')
        else:
            print(' ', end='')
            for i in range(0, index + 1):
                print(val[i], end='')
            print(';')
            break

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

# 윗 : 흰
# 아래 : 노랑
# 앞 : 빨강
# 뒷 : 오렌지
# 왼 : 초록
# 오 : 파랑


for _ in range(int(input().strip())):
    top = [['w'] * 3 for _ in range(3)]
    bottom = [['y'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    rear = [['o'] * 3 for _ in range(3)]
    left = [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]

    n = int(input().strip())
    spins = input().strip().split()

    for spin in spins:
        where, how = list(spin)

        if where == 'L':
            if how == '+':
                left[0][0], left[0][2] = left[0][2], left[0][0]
                left[0][0], left[2][2] = left[2][2], left[0][0]
                left[0][0], left[2][0] = left[2][0], left[0][0]

                left[1][0], left[0][1] = left[0][1], left[1][0]
                left[1][0], left[1][2] = left[1][2], left[1][0]
                left[1][0], left[2][1] = left[2][1], left[1][0]

                top[0][0], front[0][0] = front[0][0], top[0][0]
                top[1][0], front[1][0] = front[1][0], top[1][0]
                top[2][0], front[2][0] = front[2][0], top[2][0]

                top[0][0], bottom[0][0] = bottom[0][0], top[0][0]
                top[1][0], bottom[1][0] = bottom[1][0], top[1][0]
                top[2][0], bottom[2][0] = bottom[2][0], top[2][0]

                top[0][0], rear[2][2] = rear[2][2], top[0][0]
                top[1][0], rear[1][2] = rear[1][2], top[1][0]
                top[2][0], rear[0][2] = rear[0][2], top[2][0]
            if how == '-':
                left[0][0], left[2][0] = left[2][0], left[0][0]
                left[0][0], left[2][2] = left[2][2], left[0][0]
                left[0][0], left[0][2] = left[0][2], left[0][0]
                left[1][0], left[2][1] = left[2][1], left[1][0]
                left[1][0], left[1][2] = left[1][2], left[1][0]
                left[1][0], left[0][1] = left[0][1], left[1][0]

                top[0][0], rear[2][2] = rear[2][2], top[0][0]
                top[1][0], rear[1][2] = rear[1][2], top[1][0]
                top[2][0], rear[0][2] = rear[0][2], top[2][0]
                top[0][0], bottom[0][0] = bottom[0][0], top[0][0]
                top[1][0], bottom[1][0] = bottom[1][0], top[1][0]
                top[2][0], bottom[2][0] = bottom[2][0], top[2][0]
                top[0][0], front[0][0] = front[0][0], top[0][0]
                top[1][0], front[1][0] = front[1][0], top[1][0]
                top[2][0], front[2][0] = front[2][0], top[2][0]

        if where == 'R':
            if how == '+':
                right[0][0], right[0][2] = right[0][2], right[0][0]
                right[0][0], right[2][2] = right[2][2], right[0][0]
                right[0][0], right[2][0] = right[2][0], right[0][0]
                right[1][0], right[0][1] = right[0][1], right[1][0]
                right[1][0], right[1][2] = right[1][2], right[1][0]
                right[1][0], right[2][1] = right[2][1], right[1][0]

                top[2][2], rear[0][0] = rear[0][0], top[2][2]
                top[1][2], rear[1][0] = rear[1][0], top[1][2]
                top[0][2], rear[2][0] = rear[2][0], top[0][2]
                top[2][2], bottom[2][2] = bottom[2][2], top[2][2]
                top[1][2], bottom[1][2] = bottom[1][2], top[1][2]
                top[0][2], bottom[0][2] = bottom[0][2], top[0][2]
                top[2][2], front[2][2] = front[2][2], top[2][2]
                top[1][2], front[1][2] = front[1][2], top[1][2]
                top[0][2], front[0][2] = front[0][2], top[0][2]
            if how == '-':
                right[0][0], right[2][0] = right[2][0], right[0][0]
                right[0][0], right[2][2] = right[2][2], right[0][0]
                right[0][0], right[0][2] = right[0][2], right[0][0]
                right[1][0], right[2][1] = right[2][1], right[1][0]
                right[1][0], right[1][2] = right[1][2], right[1][0]
                right[1][0], right[0][1] = right[0][1], right[1][0]

                top[2][2], front[2][2] = front[2][2], top[2][2]
                top[1][2], front[1][2] = front[1][2], top[1][2]
                top[0][2], front[0][2] = front[0][2], top[0][2]
                top[2][2], bottom[2][2] = bottom[2][2], top[2][2]
                top[1][2], bottom[1][2] = bottom[1][2], top[1][2]
                top[0][2], bottom[0][2] = bottom[0][2], top[0][2]
                top[2][2], rear[0][0] = rear[0][0], top[2][2]
                top[1][2], rear[1][0] = rear[1][0], top[1][2]
                top[0][2], rear[2][0] = rear[2][0], top[0][2]

        if where == 'F':
            if how == '+':
                front[0][0], front[0][2] = front[0][2], front[0][0]
                front[0][0], front[2][2] = front[2][2], front[0][0]
                front[0][0], front[2][0] = front[2][0], front[0][0]
                front[1][0], front[0][1] = front[0][1], front[1][0]
                front[1][0], front[1][2] = front[1][2], front[1][0]
                front[1][0], front[2][1] = front[2][1], front[1][0]

                top[2][0], right[0][0] = right[0][0], top[2][0]
                top[2][1], right[1][0] = right[1][0], top[2][1]
                top[2][2], right[2][0] = right[2][0], top[2][2]
                top[2][0], bottom[0][2] = bottom[0][2], top[2][0]
                top[2][1], bottom[0][1] = bottom[0][1], top[2][1]
                top[2][2], bottom[0][0] = bottom[0][0], top[2][2]
                top[2][0], left[2][2] = left[2][2], top[2][0]
                top[2][1], left[1][2] = left[1][2], top[2][1]
                top[2][2], left[0][2] = left[0][2], top[2][2]
            if how == '-':
                front[0][0], front[2][0] = front[2][0], front[0][0]
                front[0][0], front[2][2] = front[2][2], front[0][0]
                front[0][0], front[0][2] = front[0][2], front[0][0]
                front[1][0], front[2][1] = front[2][1], front[1][0]
                front[1][0], front[1][2] = front[1][2], front[1][0]
                front[1][0], front[0][1] = front[0][1], front[1][0]

                top[2][0], left[2][2] = left[2][2], top[2][0]
                top[2][1], left[1][2] = left[1][2], top[2][1]
                top[2][2], left[0][2] = left[0][2], top[2][2]
                top[2][0], bottom[0][2] = bottom[0][2], top[2][0]
                top[2][1], bottom[0][1] = bottom[0][1], top[2][1]
                top[2][2], bottom[0][0] = bottom[0][0], top[2][2]
                top[2][0], right[0][0] = right[0][0], top[2][0]
                top[2][1], right[1][0] = right[1][0], top[2][1]
                top[2][2], right[2][0] = right[2][0], top[2][2]

        if where == 'B':
            if how == '+':
                rear[0][0], rear[0][2] = rear[0][2], rear[0][0]
                rear[0][0], rear[2][2] = rear[2][2], rear[0][0]
                rear[0][0], rear[2][0] = rear[2][0], rear[0][0]
                rear[1][0], rear[0][1] = rear[0][1], rear[1][0]
                rear[1][0], rear[1][2] = rear[1][2], rear[1][0]
                rear[1][0], rear[2][1] = rear[2][1], rear[1][0]

                top[0][2], left[0][0] = left[0][0], top[0][2]
                top[0][1], left[1][0] = left[1][0], top[0][1]
                top[0][0], left[2][0] = left[2][0], top[0][0]
                top[0][2], bottom[2][0] = bottom[2][0], top[0][2]
                top[0][1], bottom[2][1] = bottom[2][1], top[0][1]
                top[0][0], bottom[2][2] = bottom[2][2], top[0][0]
                top[0][2], right[2][2] = right[2][2], top[0][2]
                top[0][1], right[1][2] = right[1][2], top[0][1]
                top[0][0], right[0][2] = right[0][2], top[0][0]
            if how == '-':
                rear[0][0], rear[2][0] = rear[2][0], rear[0][0]
                rear[0][0], rear[2][2] = rear[2][2], rear[0][0]
                rear[0][0], rear[0][2] = rear[0][2], rear[0][0]
                rear[1][0], rear[2][1] = rear[2][1], rear[1][0]
                rear[1][0], rear[1][2] = rear[1][2], rear[1][0]
                rear[1][0], rear[0][1] = rear[0][1], rear[1][0]

                top[0][2], right[2][2] = right[2][2], top[0][2]
                top[0][1], right[1][2] = right[1][2], top[0][1]
                top[0][0], right[0][2] = right[0][2], top[0][0]
                top[0][2], bottom[2][0] = bottom[2][0], top[0][2]
                top[0][1], bottom[2][1] = bottom[2][1], top[0][1]
                top[0][0], bottom[2][2] = bottom[2][2], top[0][0]
                top[0][2], left[0][0] = left[0][0], top[0][2]
                top[0][1], left[1][0] = left[1][0], top[0][1]
                top[0][0], left[2][0] = left[2][0], top[0][0]

        if where == 'U':
            if how == '+':
                top[0][0], top[0][2] = top[0][2], top[0][0]
                top[0][0], top[2][2] = top[2][2], top[0][0]
                top[0][0], top[2][0] = top[2][0], top[0][0]
                top[1][0], top[0][1] = top[0][1], top[1][0]
                top[1][0], top[1][2] = top[1][2], top[1][0]
                top[1][0], top[2][1] = top[2][1], top[1][0]

                front[0][0], left[0][0] = left[0][0], front[0][0]
                front[0][1], left[0][1] = left[0][1], front[0][1]
                front[0][2], left[0][2] = left[0][2], front[0][2]
                front[0][0], rear[0][0] = rear[0][0], front[0][0]
                front[0][1], rear[0][1] = rear[0][1], front[0][1]
                front[0][2], rear[0][2] = rear[0][2], front[0][2]
                front[0][0], right[0][0] = right[0][0], front[0][0]
                front[0][1], right[0][1] = right[0][1], front[0][1]
                front[0][2], right[0][2] = right[0][2], front[0][2]
            if how == '-':
                top[0][0], top[2][0] = top[2][0], top[0][0]
                top[0][0], top[2][2] = top[2][2], top[0][0]
                top[0][0], top[0][2] = top[0][2], top[0][0]
                top[1][0], top[2][1] = top[2][1], top[1][0]
                top[1][0], top[1][2] = top[1][2], top[1][0]
                top[1][0], top[0][1] = top[0][1], top[1][0]

                front[0][0], right[0][0] = right[0][0], front[0][0]
                front[0][1], right[0][1] = right[0][1], front[0][1]
                front[0][2], right[0][2] = right[0][2], front[0][2]
                front[0][0], rear[0][0] = rear[0][0], front[0][0]
                front[0][1], rear[0][1] = rear[0][1], front[0][1]
                front[0][2], rear[0][2] = rear[0][2], front[0][2]
                front[0][0], left[0][0] = left[0][0], front[0][0]
                front[0][1], left[0][1] = left[0][1], front[0][1]
                front[0][2], left[0][2] = left[0][2], front[0][2]

        if where == 'D':
            if how == '+':
                bottom[0][0], bottom[0][2] = bottom[0][2], bottom[0][0]
                bottom[0][0], bottom[2][2] = bottom[2][2], bottom[0][0]
                bottom[0][0], bottom[2][0] = bottom[2][0], bottom[0][0]
                bottom[1][0], bottom[0][1] = bottom[0][1], bottom[1][0]
                bottom[1][0], bottom[1][2] = bottom[1][2], bottom[1][0]
                bottom[1][0], bottom[2][1] = bottom[2][1], bottom[1][0]

                front[2][0], right[2][0] = right[2][0], front[2][0]
                front[2][1], right[2][1] = right[2][1], front[2][1]
                front[2][2], right[2][2] = right[2][2], front[2][2]
                front[2][0], rear[2][0] = rear[2][0], front[2][0]
                front[2][1], rear[2][1] = rear[2][1], front[2][1]
                front[2][2], rear[2][2] = rear[2][2], front[2][2]
                front[2][0], left[2][0] = left[2][0], front[2][0]
                front[2][1], left[2][1] = left[2][1], front[2][1]
                front[2][2], left[2][2] = left[2][2], front[2][2]
            if how == '-':
                bottom[0][0], bottom[2][0] = bottom[2][0], bottom[0][0]
                bottom[0][0], bottom[2][2] = bottom[2][2], bottom[0][0]
                bottom[0][0], bottom[0][2] = bottom[0][2], bottom[0][0]
                bottom[1][0], bottom[2][1] = bottom[2][1], bottom[1][0]
                bottom[1][0], bottom[1][2] = bottom[1][2], bottom[1][0]
                bottom[1][0], bottom[0][1] = bottom[0][1], bottom[1][0]

                front[2][0], left[2][0] = left[2][0], front[2][0]
                front[2][1], left[2][1] = left[2][1], front[2][1]
                front[2][2], left[2][2] = left[2][2], front[2][2]
                front[2][0], rear[2][0] = rear[2][0], front[2][0]
                front[2][1], rear[2][1] = rear[2][1], front[2][1]
                front[2][2], rear[2][2] = rear[2][2], front[2][2]
                front[2][0], right[2][0] = right[2][0], front[2][0]
                front[2][1], right[2][1] = right[2][1], front[2][1]
                front[2][2], right[2][2] = right[2][2], front[2][2]

    for i in top:
        for q in i:
            print(q, end='')
        print()

import sys

sys.setrecursionlimit(10 ** 6)

# N : 시험장 개수
# Ai : i번 시험장에 있는 응시자 수
# B : 총 감독관이 감시할 수 있는 수
# C : 부 감독관이 감시할 수 있는 수

N = int(input())
list_A = list(map(int, input().strip().split(' ')))
B, C = map(int, input().strip().split(' '))

result = 0
for item in list_A:
    num = item - B
    # 총 감독관
    result += 1

    # 부 감독관
    if num > 0:
        if num % C == 0:
            result += (num // C)
        else:
            result += (num // C) + 1

print(result)

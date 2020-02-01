import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().strip().split())

data = {}
data2 = {}
for i in range(N):
    mon = input().strip()
    data[mon] = i + 1

line = list(data.keys())
for i in range(M):
    tmp = input().strip()
    # 숫자
    if tmp.isdecimal():
        print(line[int(tmp) - 1])
    # 문자
    else:
        print(data[tmp])

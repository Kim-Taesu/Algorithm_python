import sys

sys.setrecursionlimit(10 ** 6)

# 최소 1개의 모음, 두 개의 자음
# 증가하는 순서로 배열

filt = [ord('a') - 97, ord('e') - 97, ord('i') - 97, ord('o') - 97, ord('u') - 97]


input = sys.stdin.readline

L, C = map(int, input().strip().split())
alpha = input().strip().split()

for i in range(len(alpha)):
    alpha[i] = ord(alpha[i]) - 97
alpha.sort()
check = [0] * 26
def dfs(val, arr, ja, mo):
    if len(arr) == L:
        if mo < 1 or ja < 2: return
        for i in arr:
            print(chr(i + 97), end='')
        print()

    check[val] = True
    for i in alpha:
        if check[i]: continue
        if val > i: continue

        arr.append(i)
        if i in filt:
            dfs(i, arr, ja, mo+1)
        else:
            dfs(i, arr, ja+1, mo)
        arr.pop()

    check[val] = False


while alpha:
    val = alpha.pop(0)
    arr = []
    arr.append(val)
    if val in filt:
        dfs(val, arr, 0, 1)
    else:
        dfs(val, arr, 1, 0)

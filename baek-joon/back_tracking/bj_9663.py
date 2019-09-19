import sys
sys.setrecursionlimit(10**6)

N = int(input())

count = 0



def check(checkRow,col):
    for i in range(1,checkRow):
        if col[i]==col[checkRow]:return False
        if abs(col[i]-col[checkRow]) == abs(i-checkRow): return False
    return True


def dfs(row, col):
    if (row > N):
        global count
        count += 1
    else:
        for i in range(1, N + 1):
            col[row] = i
            if check(row,col):
                dfs(row+1,col)
            else:
                col[row]=0

for i in range(N):
    col = [0] * (N + 1)
    col[1] = i + 1
    dfs(2, col)

print(count)

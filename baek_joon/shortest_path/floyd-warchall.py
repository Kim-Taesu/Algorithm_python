import sys

from baek_joon.mst.config import *

INF = sys.maxsize
arr = [[INF] * V for _ in range(V)]

for DATA in DATA_LIST:
    x, y, w = DATA
    arr[x][y] = w

print('초기 거리')
for a in arr:
    for i in a:
        if i == sys.maxsize:
            print(-1, end='\t')
        else:
            print(i, end='\t')
    print()
print()

for k in range(V):
    for i in range(V):
        for j in range(V):
            if arr[i][k] != INF and arr[k][j] != INF:
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

print('플로이드-와샬 적용')
for a in arr:
    for i in a:
        if i == sys.maxsize:
            print(-1, end='\t')
        else:
            print(i, end='\t')
    print()

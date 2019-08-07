# 친구 관계를 저장하고
# node에서 개수 세기

import sys

INF = sys.maxsize

input = sys.stdin.readline


def getParent(node, f1):
    # print(node,f1)
    if node[f1][0] == f1: return f1
    result = getParent(node, node[f1][0])
    return result


def union(node, f1, f2):
    f1 = getParent(node, f1)
    f2 = getParent(node, f2)

    if f1 > f2:
        # node[f1] = f2
        node[f1] = (f2, node[f2][1] + node[f1][1])
        node[f2] = (f2, node[f1][1])
        return f2
    else:
        # node[f2] = f1
        node[f1] = (f1, node[f1][1] + node[f2][1])
        node[f2] = (f1, node[f1][1])
        return f1


for _ in range(int(input().strip())):
    r = int(input().strip())

    node = {}
    for _ in range(r):
        f1, f2 = input().strip().split()
        if f1 not in node:
            node[f1] = (f1, 1)
        if f2 not in node:
            node[f2] = (f2, 1)
        par = union(node, f1, f2)

        # print(node)
        print(node[par][1])

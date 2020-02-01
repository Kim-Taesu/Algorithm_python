# 친구 관계를 저장하고
# node에서 개수 세기

import sys

INF = sys.maxsize

input = sys.stdin.readline


def getParent(num):
    if node[num] == num: return num
    node[num] = getParent(node[num])
    return node[num]


def union(f1, f2):
    f1 = getParent(f1)
    f2 = getParent(f2)

    if f1 != f2:
        node[f1] = f2
        nodeWeight[f2] += nodeWeight[f1]
        nodeWeight[f1] = 1

    return nodeWeight[f2]


for _ in range(int(input().strip())):
    r = int(input().strip())

    node = []
    nodeWeight = []

    for i in range(r * 2):
        node.append(i)
        nodeWeight.append(1)
    dict = {}
    count = 0
    for _ in range(r):
        f1, f2 = input().strip().split()
        if not f1 in dict:
            dict[f1] = count
            count += 1
        a = dict[f1]

        if not f2 in dict:
            dict[f2] = count
            count += 1
        b = dict[f2]

        print(union(a, b))

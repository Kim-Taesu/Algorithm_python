import sys

INF = sys.maxsize

input = sys.stdin.readline
V, E = map(int, input().strip().split())

heap = []
for _ in range(E):
    start, end, weight = map(int, input().strip().split())
    heap.append((start, end, weight))

heap.sort(key=lambda a: a[2])

# print(heap)

node = [0]
for i in range(1, V + 1):
    node.append(i)

sum = 0


def getParent(node, param):
    if node[param] == param: return param
    result = getParent(node, node[param])
    return result
    pass


def findNode(node, param, param1):
    param = getParent(node, param)
    param1 = getParent(node, param1)
    if param1 == param:
        return True
    else:
        return False
    pass


def unionNode(node, param, param1):
    param = getParent(node, param)
    param1 = getParent(node, param1)
    if param > param1:
        node[param] = param1
    else:
        node[param1] = param
    pass


for i in range(E):
    if not findNode(node, heap[i][0], heap[i][1]):
        sum += heap[i][2]
        unionNode(node, heap[i][0], heap[i][1])

print(sum)
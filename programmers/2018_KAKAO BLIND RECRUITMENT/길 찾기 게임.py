import sys

sys.setrecursionlimit(10 ** 6)


def order(node, postList, preList):
    postList.append(node.data)
    if node.left is not None:
        order(node.left, postList, preList)
    if node.right is not None:
        order(node.right, postList, preList)
    preList.append(node.data)


class tree:
    def __init__(self, dataList):
        self.data = max(dataList, key=lambda x: x[1])
        leftList = list(filter(lambda x: x[0] < self.data[0], dataList))
        rightList = list(filter(lambda x: x[0] > self.data[0], dataList))
        if leftList != []:
            self.left = tree(leftList)
        else:
            self.left = None

        if rightList != []:
            self.right = tree(rightList)
        else:
            self.right = None


def solution(nodeinfo):
    answer = []

    root = tree(nodeinfo)
    pre = []
    post = []
    order(root, pre, post)
    print(pre)
    print(list(map(lambda x: nodeinfo.index(x) + 1, pre)))
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, pre)))
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, post)))

    return answer
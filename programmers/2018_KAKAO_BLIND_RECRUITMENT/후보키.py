from itertools import combinations


def solution(relation):
    answer = 0

    indexs = []
    checkList = []

    colSize = len(relation[0])
    rowSize = len(relation)

    for i in range(1, colSize + 1):
        indexs.extend([set(k) for k in combinations([j for j in range(colSize)], i)])

    for index in indexs:
        check = set()
        for r in relation:
            tmp = ''
            for i in index:
                tmp += r[i]
            check.add(tmp)
        if len(check) == rowSize: checkList.append(index)
    print(checkList)

    delSet = set()

    for comp1 in checkList:
        for ind, comp2 in enumerate(checkList):
            if comp1.issubset(comp2) and comp1 != comp2:
                delSet.add(checkList.index(comp2))

    print(delSet)

    return len(checkList) - len(delSet)

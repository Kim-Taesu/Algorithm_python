from itertools import combinations


def solution(relation):
    answer = 0

    indexs = []
    checkList = []

    if len(relation) > 0:
        colSize = len(relation[0])
        rowSize = len(relation)

        # 모든 컬럼의 조합 구하기 (Set형태)
        for i in range(1, colSize + 1):
            # append는 런타임에러가 뜸 append와 extend 비교하여 알아둘 것
            indexs.extend([set(k) for k in combinations([j for j in range(colSize)], i)])

        for index in indexs:
            check = set()
            for r in range(rowSize):
                tmp = ''
                for i in index:
                    tmp += relation[r][i]
                check.add(tmp)

            if len(check) == rowSize: checkList.append(index)

        delSet = set()

        for comp1 in checkList:
            for ind, comp2 in enumerate(checkList):
                if comp1.issubset(comp2) and comp1 != comp2:
                    delSet.add(checkList.index(comp2))

        answer = len(checkList) - len(delSet)

        print(checkList)

        return answer
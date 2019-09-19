# 간선을 거리가 짧은 순서대로 그래프에 포함
# 적은 비용으로 연결만 시키면 되기 때문에 모든 간선 정보를 오름차순 정렬한다.
# 거리 기준으로 오름차순 정렬
# 정렬 순서에 맞게 그래프에 포함하면서 사이클 확인

def getParent(node, num1):
    if node[num1] == num1: return num1
    result = getParent(node, node[num1])
    return result


def unionNode(node, num1, num2):
    num1 = getParent(node, num1)
    num2 = getParent(node, num2)
    if num1 > num2:
        node[num1] = num2
    else:
        node[num2] = num1


def findNode(node, num1, num2):
    num1 = getParent(node, num1)
    num2 = getParent(node, num2)
    if num1 == num2:
        return 1
    else:
        return 0


V = 7
E = 11

EList = []
EList.append((1, 7, 12))
EList.append((1, 4, 28))
EList.append((1, 2, 67))
EList.append((1, 5, 17))
EList.append((2, 4, 24))
EList.append((2, 5, 62))
EList.append((3, 5, 20))
EList.append((3, 6, 37))
EList.append((4, 7, 13))
EList.append((5, 6, 45))
EList.append((5, 7, 73))

EList.sort(key=lambda weight: weight[2])
print(EList)

node = [0]
for i in range(1, V + 1):
    node.append(i)

sum = 0
for i in range(E):
    if not findNode(node, EList[i][0], EList[i][1]):
        sum += EList[i][2]
        unionNode(node, EList[i][0], EList[i][1])

print(sum)

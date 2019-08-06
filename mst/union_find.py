# union 할 때 부모는 작은 값이 된다.

node = [0] * 11

for i in range(1, 11):
    node[i] = i


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

def findNode(node, num1,num2):
    num1=getParent(node,num1)
    num2 = getParent(node,num2)
    if num1==num2: return '연결'
    else: return '연결x'
    pass



unionNode(node, 1, 2)
unionNode(node, 2, 3)
unionNode(node, 3, 4)
unionNode(node, 5, 6)
unionNode(node, 6, 7)
unionNode(node, 7, 8)
print('1과 5는 연결?',findNode(node,1,5))
unionNode(node, 1, 5)
print('1과 5는 연결?',findNode(node,1,5))
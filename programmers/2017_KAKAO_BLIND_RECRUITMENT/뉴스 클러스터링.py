import math
from string import ascii_lowercase

alpha = list(ascii_lowercase)


def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    list1 = list(str1)
    list2 = list(str2)

    set1 = []
    set2 = []

    for i in range(len(list1) - 1):
        if list1[i] in alpha and list1[i + 1] in alpha:
            set1.append(list1[i] + list1[i + 1])
    for i in range(len(list2) - 1):
        if list2[i] in alpha and list2[i + 1] in alpha:
            set2.append(list2[i] + list2[i + 1])

    # 교집합
    result1 = 0
    # 합집합
    result2 = len(set2)

    del1 = []
    print(set1, set2)

    for s1 in set1:
        if s1 in set2:
            del1.append(s1)
            set2.remove(s1)
            result1 += 1

    set2.extend(del1)
    print(set1, set2, result1)

    for s2 in set2:
        if s2 in set1:
            set1.remove(s2)

    set2.extend(set1)
    result2 = len(set2)

    if result2 == 0:
        answer = 65536
    else:
        answer = math.floor((result1 / result2) * 65536)

    return answer

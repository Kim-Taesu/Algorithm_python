from collections import deque

child_info = {}
parent_info = {}
partner_info = {}
score = {}
N, M = map(int, input().strip().split(' '))
first = input().strip()
for _ in range(N):
    c, p1, p2 = input().strip().split(' ')

    # 자식 정보
    if p1 not in child_info:
        child_info[p1] = {c}
    else:
        child_info[p1].add(c)
    if p2 not in child_info:
        child_info[p2] = {c}
    else:
        child_info[p2].add(c)

    # 부모 정보
    parent_info[c] = {p1, p2}

    # 배우자 정보
    if p1 not in partner_info:
        partner_info[p1] = {p2}
    else:
        partner_info[p1].add(p2)
    if p2 not in partner_info:
        partner_info[p2] = {p1}
    else:
        partner_info[p2].add(p1)

    # 혈통 계승 점수 초기화
    if p1 not in score:
        score[p1] = -1
    if p2 not in score:
        score[p2] = -1
    if c not in score:
        score[c] = -1

want = {}
for _ in range(M):
    m = (input().strip())
    want[m] = 0

# for key in score.keys():
#     if key not in parent_info:
#         score[key] = -1
score[first] = 1

queue = deque()
queue.append(first)
while queue:
    node = queue.popleft()

    # 배우자가 없으면 자식도 없음
    if node not in partner_info:
        continue

    node_partners = partner_info[node]

    # 해당 노드의 배우자 리스트
    for node_partner in node_partners:

        for child in child_info[node]:
            # 같은 자식이면
            if child in child_info[node_partner]:
                partner_check = score[node_partner] / 2 if score[node_partner] != -1 else 0
                # 자식 혈통 순위 업데이트
                score[child] = score[node] / 2 + partner_check
                if child in want:
                    want[child] = score[child]
                queue.append(child)

# pprint.pprint(partner_info)
# pprint.pprint(child_info)
# pprint.pprint(parent_info)
# pprint.pprint(score)
# print(want)
want = sorted(want.items(), key=lambda x: -x[1])
print(want[0][0])

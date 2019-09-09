import sys

input = sys.stdin.readline


def solution(record):
    people = {}
    message = []
    answer = []

    for line in record:
        tmp = line.split()

        if tmp[0] == 'Enter':
            people[tmp[1]] = tmp[2]
            message.append((tmp[1], "in"))
            pass
        if tmp[0] == 'Leave':
            message.append((tmp[1], "out"))
            pass
        if tmp[0] == 'Change':
            people[tmp[1]] = tmp[2]
            pass

    for m in message:
        if m[1] == "in":
            answer.append(people[m[0]] + '님이 들어왔습니다.')
            pass
        else:
            answer.append(people[m[0]] + '님이 나갔습니다.')
            pass

    return answer
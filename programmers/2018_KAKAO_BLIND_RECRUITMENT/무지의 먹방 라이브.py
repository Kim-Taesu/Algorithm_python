def solution(food_times, k):
    answer = -1
    index = []
    l = len(food_times)
    i = 0

    # (food, index)
    for f in food_times:
        index.append((f, i))
        i += 1

    index.sort()
    # print(index)

    before = 0

    for i in index:
        tmp = (i[0] - before) * l
        before = i[0]
        # print(k,tmp,before)
        # print(food_times)

        if tmp <= k:
            k -= tmp

        else:
            k %= l
            cnt = -1
            for f in range(len(food_times)):
                if food_times[f] == ('n', 'n'):
                    continue
                else:
                    cnt += 1
                if cnt == k:
                    answer = f + 1
                    break
            break

        food_times[i[1]] = ('n', 'n')
        l -= 1

    return answer

def solution(n, t, m, timetable):
    answer = ''
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()
    result = []
    bustime = 540
    for i in range(n):
        bustime = 540 + i * t
        print(bustime)
        print(timetable)
        print(result)

        delArr = []
        for time in timetable:
            if bustime >= time:
                last = time
                delArr.append(time)
                if len(delArr) == m: break

        if len(delArr) == m:
            result.append(last - 1)
        else:
            result.append(bustime)
        for d in delArr:
            timetable.remove(d)

    kts = max(result)
    h, m = kts // 60, kts % 60
    return '%02d:%02d' % (h, m)

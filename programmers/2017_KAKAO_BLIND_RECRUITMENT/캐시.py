def solution(cacheSize, cities):
    answer = 0
    arr = []

    for city in cities:
        city = city.lower()
        # cache hit
        if city in arr:
            answer += 1
            index = arr.index(city)
            arr.remove(city)
            arr.insert(0, city)
            pass

        # cache miss
        else:
            answer += 5
            if cacheSize == 0: continue
            if cacheSize > 0 and len(arr) == cacheSize:
                arr.pop()
                arr.insert(0, city)
            else:
                arr.insert(0, city)

    return answer
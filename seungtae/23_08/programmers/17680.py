def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.upper()
        if city in cache:
            index = cache.index(city)
            cache.pop(index)
            cache.append(city)
            answer += 1
        else:
            if cacheSize == 0:
                pass
            elif len(cache) >= cacheSize:
                cache.pop(0)
                cache.append(city)
            else:
                cache.append(city)
            answer += 5
    return answer
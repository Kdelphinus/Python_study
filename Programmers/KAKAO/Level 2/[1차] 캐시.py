"""2018 KAKAO BLIND RECRUITMENT"""

"""
LRU(Least Recently Used) 알고리즘
-> 가장 오랫동안 사용하지 않은 페이지를 제거하는 알고리즘
"""


def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:  # 캐시가 없다면 모두 5초씩 걸린다
        return len(cities) * 5

    cache = []
    for city in cities:
        city = city.lower()  # 모두 소문자로 통일

        if city in cache:  # 캐시에 남아있다면
            answer += 1  # 1초 걸리고
            cache.pop(cache.index(city))  # 원래 있던 자리에서 빼고
            cache.append(city)  # 가장 최근에 사용한 것으로 추가
        else:  # 캐시에 없다면
            answer += 5  # 5초 걸리고
            if len(cache) == cacheSize:  # 캐시가 다 차있다면
                cache.pop(0)  # 가장 오래된 것을 제거
            cache.append(city)  # 가장 최근에 사용한 것으로 추가

    return answer


# ---------------------------------------------------------------------------------
"""deque의 기능 활용"""


def use_maxlen(cacheSize, cities):
    import collections

    cache = collections.deque(maxlen=cacheSize)  # maxlen으로 길이를 제한할 수 있다
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time


print(
    solution(
        3,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
        ],
    )
)  # 50

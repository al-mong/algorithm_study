# LRU 알고리즘
# 대소문자 유의 -> lowercase로
# 실행시간 = 큐에 없으면 5 있으면 1
# Set? Set이 나을라나. Set이 메모리는 큰데 해시구조라서 시간복잡도는 1임
# 근데 Set은 순서가 없기 때문에, 최근인지 확인이 안 됨
# deque로 해볼까? 앞에다 집어넣고, 매 번 캐시 이전부터 확인하기.
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    que = deque()
    for city in cities:
        city = city.lower()
        for i in range(len(que)-1, -1, -1):
            if que[i] == city:
                answer += 1
                que.remove(city)
                break
        else:
            answer += 5
        que.appendleft(city)

        if len(que) > cacheSize:
            que.pop()

    return answer
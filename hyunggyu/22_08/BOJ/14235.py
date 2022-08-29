# 거점을 두고 선물을 준다.
# 선물들의 가치들을 출력하기
# 없다면 -1출력
import heapq
T = int(input())
# h를 힙 함수로 활용
h = []
for t in range(T):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if len(h) < 1:
            # indexError 방지
            print('-1')
        else:
            tmp = heapq.heappop(h)
            print(tmp[1])
    # a가 0이 라면 아이들을 만나는것
    # a가 들어오고 a개의 숫자가 들어온다. 그다음 들어오는 것은 선물의 가치
    # 선물은 큰 것부터 준다.
    else:
        for i in range(a[0]):
            # 선물의 개수만큼 최대 힙을 통해 값 부여
            heapq.heappush(h, (-a[i + 1], a[i + 1]))
        

        

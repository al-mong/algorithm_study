# 아이디어 정리부터
# 먼 곳의 택배부터 쳐내야하는 건 확실
# 수거와 배달의 우선순위??
# 근데 결국 먼 곳 먼저 배달하고 수거해야 하는 건 확실함.
# 숫자 계산만 하면 안되나?
# 갔다 올 집 위치를 설정하고
# 갔다 왔을 때의 그래프 최신화만 되면 될 거 같은디
# 누적합도 괜찮을듯?? 한번 해볼까

def solution(cap, n, deliveries, pickups):
    answer = 0
    ac_d = [deliveries[-1]]                                 # 리스트를 거꾸로 한 누적합으로 할 거라서, 마지막 값을 넣어줌
    ac_p = [pickups[-1]]                                    # 위와 동일
    for i in range(1, n):                                   # 순회하면서 누적합 채워주기
        ac_d.append(deliveries[n-i-1]+ac_d[i-1])
        ac_p.append(pickups[n-i-1]+ac_p[i-1])
    
    tot = 0                                                 # 지금까지 배달한(수거한) 물건 총량
    start = 0                                               # 탐색 시작할 기준 인덱스
    while tot < ac_d[-1] or tot < ac_p[-1]:                 # 누적합의 마지막값이 총량이므로, 총량들보다 토탈이 커질때까지 반복
        for i in range(start, n):                           # 기준 인덱스 기준으로 탐색
            if ac_d[i] > tot or ac_p[i] > tot:              # 만약 현재 인덱스값이 토탈보다 크면, 배달할 게 남아있다는 것이기 때문에
                start = i                                   # 현재 위치가 기준 인덱스가 되고
                answer += (n-i)                             # 이동한 거리만큼 정답에 더해줌
                break
        tot += cap                                          # 한 번 돌았으니, 그만큼 배달한(수거한) 물량의 총량을 늘려줌

        
    
    return answer*2                                         # 최종적으로는 왕복이 기준이기 때문에 거리 x 2를 반환함


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1,0,2,0,1,0,2],[0,2,0,1,0,2,0]))

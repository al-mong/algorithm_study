def solution(cap, n, deliveries, pickups):
    answer = 0
    temp = -1
    d_max_index = n-1
    p_max_index = n-1
    
    while temp != 0:        
        temp = 0

        # 딜리버리
        d_count = 0
        d_first = True
        for d in range(d_max_index, -1, -1):
            # 0 이면 패스
            if deliveries[d] == 0:
                continue            
            # 0 말고 가장 먼 거리
            if d_first:
                d_first = False
                temp = d + 1
                
            
            if d_count + deliveries[d] > cap:
                deliveries[d] -= (cap - d_count)
                d_count = cap
                break
            else:
                d_count += deliveries[d]
                deliveries[d] = 0
                if d_count == cap:
                    break
        d_max_index = d
        
        
        # 픽업
        p_count = 0
        p_first = True
        for p in range(p_max_index, -1, -1):
            # 0 이면 패스
            if pickups[p] == 0:
                continue
            # 0 말고 가장 먼 거리
            if p_first:
                p_first = False
                temp = max(temp, p + 1)
                
            if p_count + pickups[p] > cap:
                pickups[p] -= (cap - p_count)
                p_count = cap
                break
            else:
                p_count += pickups[p]
                pickups[p] = 0
                if p_count == cap:
                    break
        p_max_index = p
        
        if p_count != 0 or d_count !=0:
            answer += 2*temp
        else:
            answer += temp
    return answer
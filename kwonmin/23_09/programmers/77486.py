# 칫솔 한 개당 이익은 100원으로 정해져 있음
# 즉 어마운트 * 100 하면 이익
# 이익을 타고 올라가는 과정
# 세그먼트 같은 느낌인데
# 느리게 갱신되는?
# 어? 이거 레이지 세그먼트인가? 흠?
# 그정도로 거창한 것 같지는 않고;;
# 이미 트리 구조니까
# 리프노드부터 올라오면서 큐에 단 한번씩만 계산하게 하는 게 맞을 듯?
# 결국 부모 노드가 누구인지는 알고 있으니까
# 부모 노드만 갱신하는 방식

# 이거 느리게 갱신하면 안되네
# 바로 갱신해야되네
# 한번에 하면, 그 1의 단위 없어질 때 어쩌구 조건 때문에 문제가 생길 듯

# 그럼 간단한 조작만 하면 될 듯?
# enroll이랑 referral 이랑 이거 하면서 인덱스 처리를 어떻게 할지.
# 결국 해당값에 맞는 enroll로 찾아가기 가 핵심
# 매핑하는 게 맞을듯.

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    idx = defaultdict(int)
    idx["-"] = -1
    for i in range(len(enroll)):
        idx[enroll[i]] = i

    # 추가로 뭘 안해도 찾아지지 않을까?

    def dfs(x,money):
        if x == -1:
            return
        
        dt = money // 10
        if dt:
            mine = money - dt
            answer[x] += mine
            dfs(idx[referral[x]], dt)
        else:
            answer[x] += money
    
    for j in range(len(seller)):
        dfs(idx[seller[j]], amount[j]*100)
    
    return answer



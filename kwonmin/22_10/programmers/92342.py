# 모든 경우의 수 구하기
# 최대값과 크거나 같으면 갱신
# 비열한 놈들
# 10 0 0 0 0 0 0 0 0 0
# 9 1 0 0 0 0 0 0 0 0 0
# 9 0 1 0 0 0 0 0 0 0 0
# 이런 식으로 쭉
# 마지막에 도달하면 나머지 다 때려부으면 됨
# 순열보다는 부분집합에 가깝나?
max_cnt = -1
answer = []
            
def solution(n, info):

    def 화살쏘기(i,s,info):
        global max_cnt
    # 대충 10발 쏘는거니까 앞에서 몇 발 쏠지를 결정
        if i == 10:
            cnt = 0
            vic_cnt = 0
            arrow_list[10] = s
            for k in range(11):
                if arrow_list[k] > info[k]:
                    cnt += (10-k)
                elif info[k]:
                    vic_cnt += (10-k)
            gap = cnt - vic_cnt
            print(gap)
            if gap > max_cnt:
                max_cnt = gap
                answer = arrow_list[:]

        else:
            arrow_list[i] = 0
            화살쏘기(i+1, s,info)
            for x in range(1,s+1):
                arrow_list[i] = x
                화살쏘기(i+1, s-x,info)

    arrow_list = [0]*11
    화살쏘기(0,n,info)
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0] ))
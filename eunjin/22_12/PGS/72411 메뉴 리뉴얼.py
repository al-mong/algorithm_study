from itertools import combinations
def solution(orders, course):
    answer = []
    for cou in range(len(course)):        #원하는 조합 개수
        ans = {}
        total = []
        for i in orders:                  #사람마다 주문한 메뉴
            a = list(combinations(i,course[cou]))
            total += a
        for j in total:
            jjj = []
            for jj in j:
                jjj.append(jj)
            jjj.sort()                    #정렬해주려고 풀었다가 다시 튜플로 묶기
            jjj = tuple(jjj)
            if jjj in ans:                #ans딕셔너리에 저장
                ans[jjj] += 1
            else:
                ans[jjj] = 1
        if len(ans) == 0:
            pass
        else:
            ansmax = max(list(ans.values()))    #제일 큰거 찾기
            if ansmax == 1 or ansmax == 0:
                pass
            else:
                for k in ans:
                    if ans[k] == ansmax:
                        toto = ''
                        for kk in range(len(k)):
                            toto += k[kk]
                        answer.append(toto)
    answer.sort()
    return answer 
    
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
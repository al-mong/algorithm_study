# 230102
def solution(k, dungeons):
    answer = -1 
    
    
    def cal(p):
        tmp_result = 0
        tmp_k = k
        for i in p:
            if tmp_k >= dungeons[i][0]:
                tmp_k -= dungeons[i][1]
                tmp_result += 1
        return tmp_result    
    
    
    def perm(i, n, r):
        nonlocal answer
        if i == r:
            answer = max(cal(p), answer)
        else:
            for j in range(i, n):
                p[i], p[j] = p[j], p[i]
                perm(i + 1, n, r)
                p[i], p[j] = p[j], p[i]
    
    
    n = len(dungeons)
    p = [i for i in range(n)]
    perm(0, n, n)
    
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))

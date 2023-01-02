from itertools import permutations

def solution(k, dungeons):
    answer = 0
    len_dungeons = len(dungeons)
    for permu in permutations(dungeons, len_dungeons):
        kk = k 
        count = 0
        for p in permu:
            if kk >= p[0]:
                kk -= p[1] 
                count += 1  
        answer = max(answer, count)  
    return answer
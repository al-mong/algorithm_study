def solution(n):
    def numToBi(num):
        bi = bin(num)
        return bi[2:] 
    answer = 0
    bi = numToBi(n)
    bi_cnt = numToBi(n).count('1')
    while True:
        n += 1
        if numToBi(n).count('1') == bi_cnt:
            break
    answer = n
        
    return answer
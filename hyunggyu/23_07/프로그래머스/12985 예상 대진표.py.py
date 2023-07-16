# 42842 Ä«Æê

def solution(n,a,b):
    round_n = 0
    a -= 1
    b -= 1
    tmp = n//2
    while a != b:
        round_n += 1
        tmp_a = 0
        tmp_b = 0
        if a >= tmp:
            tmp_a = 1
            a -= tmp
        if b >= tmp:
            tmp_b = 1
            b -= tmp
        a //= 2
        b //= 2
        tmp //= 2
        if tmp_a:
            a += tmp
        if tmp_b:
            b += tmp
    answer = round_n

    return answer
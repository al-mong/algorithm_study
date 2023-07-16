def solution(brown, yellow):
    answer = []
    if yellow == 1:
        answer = [3,3]
    else:
        for a in range(yellow//2, 0, -1):
            if yellow % a == 0:
                b = yellow // a
                if (a+b)*2+4 == brown:
                    if a > b:
                        answer = [a+2, b+2]
                    else:
                        answer = [b+2, a+2]
    return answer
from math import sqrt
def solution(brown, yellow):
    total_answer = []
    answer = []
    for i in range(int(sqrt(yellow)),0,-1):     # 36 = 6**2 처럼 루트씌운거까지만 구하기
        if yellow % i == 0:
            answer.append((i,yellow//i))
    for (a,b) in answer:
        if (a+b)*2 + 4 == brown:                # brown이랑 같을 수 밖에 없는 구조(=수식)
            total_answer.append(b+2)
            total_answer.append(a+2)
    return total_answer

print(solution(10,2)) 
print(solution(8,1)) 
print(solution(24,24)) 
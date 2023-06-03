from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    n = len(emoticons)
    digits = [10, 20, 30, 40]

    # 4 x 4 x 4 x 4 만큼의 모든 할인율 경우의 수를 반복
    for combination in product(digits, repeat=n):
        
        sign_count = 0
        revenue = 0

        # 할인율 한가지에 대해 모든 유저를 돌면서 가입자수 + 수익을 계산
        for user in users:
            temp_revenue = 0
            for i in range(n):
                if user[0] <= combination[i]:
                    temp_revenue += (emoticons[i] - emoticons[i] * combination[i] * 0.01)
                if temp_revenue >= user[1]:
                    sign_count += 1
                    break
            else:
                revenue += temp_revenue
        
        # 가입자수가 기존보다 많으면 => 가입자수와 수익을 갱신
        if sign_count > answer[0]:
            answer[0] = sign_count
            answer[1] = revenue
        # 가입자수가 기존보다 같으면 => 수익만 갱신
        elif sign_count == answer[0]:
            answer[1] = max(answer[1], revenue)
        
    return answer
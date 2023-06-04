# 브루트포스 느낌으로 접근
# 유저 최대 100명
# 할인율은 4가지 경우 = 10%, 20%, 30%, 40%
# 이모티콘은 해봤자 7개
# 100 * 4 * 7? 인가

# 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
# 이모티콘 판매액을 최대한 늘리는 것.
# 1번 목표가 우선이며, 2번 목표가 그 다음입니다.


def solution(users, emoticons):
    answer = []
    elen = len(emoticons)
    event = [0] * elen
    max_signup = 0
    max_total = 0

    def check_user(event):
        total = 0
        signup = 0
        for s, t in users:
            now = 0
            for i in range(elen):

                if event[i] >= s:
                    now += (emoticons[i] // 100 * (100-event[i]))
            if now >= t:
                signup += 1
            else:
                total += now

        return [total, signup]

    def makeEvent(start=0, end=elen):
        nonlocal max_signup
        nonlocal max_total
        if start == end:
            now_total, now_signup = check_user(event)
            if now_signup > max_signup:
                max_signup = now_signup
                max_total = now_total
            elif now_signup == max_signup:
                max_total = max(max_total, now_total)

            return
        
        for x in range(5):
            event[start] = x*10
            makeEvent(start+1, end)
    
    makeEvent()



    return [max_signup, max_total]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
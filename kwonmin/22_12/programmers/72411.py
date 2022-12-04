# 브루트포스적으로 접근
# 두 번 이상 시킨 메뉴들 모아서
# 하나의 리스트에 담아 두고
# 해당 리스트에 있는 것들로 2부터 최대N까지 순열만들어서
# 2명 이상이 주문한 메뉴 조합을 후보에 넣는다.
# 맥스랑 같을 경우에도 집어넣는다.

from itertools import combinations


def solution(orders, course):
    answer = []                                 
    menu = set()                                # set으로 중복 없애기
    alp = []                                    # 일단 알파벳 담아놓을 리스트
    for order in orders:                        # 손님 돌기
        for a in order:                         # 알파벳 꺼내는 작업
            if a in alp:                        # 2번 이상 나온 알파벳만 넣어두기
                menu.add(a)
            else:
                alp.append(a)
    
    menu = list(menu)                           # 메뉴 리스트화시키고 정렬하기
    menu.sort()

    for i in course:                            # 원하는 코스 길이만큼 콤비네이션으로 원소뽑기
        res = []
        max_cnt = 2
        for com in combinations(menu, i):       # 메뉴들 뽑기
            cnt = 0
            for order in orders:                # 주문 돌면서
                for c in com:                   # 조합에 있는 거 다들었는지 확인
                    if c not in order:          # 없으면 브레이크
                        break
                else:                           # 다 통과하면 카운트올리기
                    cnt += 1

            if cnt > max_cnt:                   # 카운트가 맥스보다 높으면
                max_cnt = cnt                   # 맥스카운트 갱신
                res.clear()                     # 기존 res 비우기
                res.append(''.join(com))        # res에 문자열로 바꾸어 넣기
            elif cnt == max_cnt:
                res.append(''.join(com))
        answer.extend(res)                      # 다 돌고나서 answer에 값 채우기
    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))

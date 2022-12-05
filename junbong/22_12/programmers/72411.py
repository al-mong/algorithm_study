from collections import defaultdict
check = defaultdict(int)


# 조합
def comb(order_list, c, n, r):
    global check
    if r == 0:
        check[''.join(c)] += 1
    elif n < r:
        return
    else:
        c[-r] = order_list[-n]
        comb(order_list, c, n - 1, r - 1)
        comb(order_list, c, n - 1, r)


def solution(orders, course):
    global check
    answer = []
    
    for order in orders:
        order_list = sorted(list(order))
        for r in course:
            c = [0] * r
            comb(order_list, c, len(order_list), r)
    
    check = dict(filter(lambda x: x[1] >= 2, check.items()))  # 주문 횟수가 2 이상인 것들만, 코스 후보: 주문 횟수
    
    print("<< 코스 후보: 주문횟수 >> ", check)
    
    cnt_set = set()  # 주문 횟수 종류
    course_info = defaultdict(list)  # 주문 횟수를 key로 하고 value를 해당하는 코스 후보들의 리스트로 함
    for key, value in check.items():  
        course_info[value].append(key)
        cnt_set.add(value)
        
    print("<< 주문 횟수: 코스 후보들의 리스트 >> ", course_info)
    print("<< 주문 횟수의 종류 >> ", cnt_set)
    
    cnt_list = sorted(list(cnt_set), reverse=True)  # 주문 횟수 내림차순 정렬
    max_cnt = {c: 0 for c in course}  # 글자 수 별 최대 주문 횟수 저장
    for cnt in cnt_list:  # 주문 횟수가 많은 것부터
        for course_cand in course_info[cnt]:  # course_cand: 코스 후보
            # 현재 후보의 주문 횟수가 코스 길이의 최대 주문 횟수보다 작다면 continue
            if cnt < max_cnt[len(course_cand)]:  
                continue
            max_cnt[len(course_cand)] = cnt  # 최대 주문 횟수 갱신
            answer.append(course_cand)  # 결과에 코스 후보 추가
    
    answer.sort()
    return answer


print("<< 결과 >> ",solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    # 코스요리 개수 n을 순회
    for n in course:

        max_count = 0                   # n개의 요리 조합 중 가장 많이 나온 횟수
        temp_answer = []                # max_count 만큼 나왔던 메뉴들
        visited = defaultdict(int)      # visited 용 defaultdict

        # 주문들 순회
        for order in orders:

            # 1. 주문의 n개짜리 모든 조합을 순회
            for johap in combinations(order, n):
                temp = "".join(sorted(johap))       # 얻어진 조합을 정렬 후 문자열로 합치기 (ex. ['C','B','A'] => 'ABC')

                if visited[temp] == 1: continue     # 조합이 defaultdict 에 방문한적이 있으면 아래의 코드를 실행하지 않음
                visited[temp] = 1                   # 조합이 defaultdict 에 방문 기록이 없으면 방문기록용 1을 할당

                # 2. 여기서부터는 해당 조합이 모든 주문 중에 몇번 포함되었는가를 count 함
                count = 0
                for order2 in orders:
                    for menu in johap:
                        if menu not in order2:
                            break
                    else:
                        count += 1

                # 3. 2번이상 등장한 조합중에
                #    카운트가 맥스카운트보다 크면 ? 여태까지 정답리스트에 있던거 싹다 리셋하고 저장 : 같으면 정답리스트에 append
                if count >= 2:
                    if count > max_count:
                        temp_answer = [temp]
                        max_count = count
                    elif count == max_count:
                        temp_answer.append(temp)

        # 4. 해당 n 에 대한 #1~3의 계산이 끝났으면 temp_answer 를 answer 에 append
        for temp_answer_item in temp_answer:
            answer.append(temp_answer_item)

    answer.sort()

    return answer

if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))

# 테스트 1 〉	통과 (0.14ms, 10.1MB)
# 테스트 2 〉	통과 (0.08ms, 10.2MB)
# 테스트 3 〉	통과 (0.24ms, 10MB)
# 테스트 4 〉	통과 (0.24ms, 10.1MB)
# 테스트 5 〉	통과 (0.26ms, 10.1MB)
# 테스트 6 〉	통과 (0.93ms, 10.4MB)
# 테스트 7 〉	통과 (0.98ms, 10MB)
# 테스트 8 〉	통과 (4.83ms, 10MB)
# 테스트 9 〉	통과 (4.95ms, 10.4MB)
# 테스트 10 〉	통과 (7.30ms, 10.3MB)
# 테스트 11 〉	통과 (3.71ms, 10.3MB)
# 테스트 12 〉	통과 (4.71ms, 10.1MB)
# 테스트 13 〉	통과 (6.81ms, 10.3MB)
# 테스트 14 〉	통과 (7.07ms, 10.3MB)
# 테스트 15 〉	통과 (13.13ms, 10.3MB)
# 테스트 16 〉	통과 (1.89ms, 10.2MB)
# 테스트 17 〉	통과 (1.02ms, 10.1MB)
# 테스트 18 〉	통과 (0.75ms, 10.2MB)
# 테스트 19 〉	통과 (0.07ms, 10MB)
# 테스트 20 〉	통과 (1.32ms, 10.2MB)
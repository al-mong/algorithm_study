# 브루트포스로 풀까 싶었는데
# 10만 이하면, 좀 곤란할듯...?
# 둘 다 정렬함
# 아닌데...흠...흠...흠...
# B를 기준으로 해야하나?
# B의 가장 작은 숫자와 A의 가장 작은 숫자를 비교함
# B가 크면 -> ㅇㅋ
# A가 크면 -> A의 가장 큰숫자 짬처리
# 이런 식으로
# 같을 때는 점수가 0이잖아?
# 흠 상관없을려나?


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    start = 0
    end = len(A)-1
    for b in B:
        if A[start] < b:
            start += 1
            answer += 1
        else:
            end -= 1

    return answer
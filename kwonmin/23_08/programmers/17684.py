# 진짜 귀찮은 유형의 문제...
# 그래도 카카오 입사시험에 나온거니까
# 풀긴 풀어야지

# 생각
# 현재 색인을 들고있는 게 맞긴할듯... Z가 26이니까 27부터 집어넣게
# 가장 긴 w를 탐색해야 함. 현재 위치 확인 -> 그다음거랑 이어진 거 있는 지 확인 -> 없으면 현재 위치걸로 펑!
# while을 써서 i값을 움직이는 형식으로 가는 게 나을까? 싶으니까 이렇게 풀어보기
# w를 탐색하는 과정이 제일 중요. A부터 Z까지 초기화 어떻게 할까? -> 이거 좀 세련된 방법 있는디;

from collections import defaultdict

def solution(msg):
    answer = []
    idxs = defaultdict(int)

    for i in range(26):
        idxs[chr(ord('A')+i)] = i+1                 # A - Z 까지 값 초기화 (1부터 26)
    
    now_idx = 27                                    # 그 다음으로 올 인덱스
    now = 0                                         # 현재 포인터 위치
    while now < len(msg):                           # 포인터가 범위 안에 있을 때 까지만
        next = 1                                    # 탐색 범위 초기화
        while now+next <= len(msg):                 # 탐색 범위가 msg 범위 안에 있도록 설정
            if idxs[msg[now:now+next]]:             # 다음 길이의 단어가 사전에 있으면
                next+=1                             # 탐색 범위 확장
            else:
                break                               # w 탐색 종료
        answer.append(idxs[msg[now:now+next-1]])    # 가장 긴 단어의 색인값 answer에 추가하기
        idxs[msg[now:now+next]] = now_idx           # 가장 긴 단어 + 1 의 단어 색인에 추가하기
        now_idx += 1                                # 다음 색인값 갱신
        now = now + next - 1                        # 포인터 이동

    return answer


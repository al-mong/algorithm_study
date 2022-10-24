# 불량 이용자를 신고하고 처리 결과 메일 발송하는 시스템
# k번 이상 신고된 유저 정지되고 신고한 모든 유저에게 신고 사실 알려줌
# id_list =id 문자열 리스트
# report = 이용자id, 신고한 id
# k = 정지기준
# answer = id리스트 순서대로 받는 메일수
def solution(id_list, report, k):
    report = list(set(report))
    ban = [0]*len(id_list)
    for i in range(len(report)):
        a,b = report[i].split()
        for j in range(len(id_list)):
            if b == id_list[j]:
                pass
                
                
    answer = []
    return answer
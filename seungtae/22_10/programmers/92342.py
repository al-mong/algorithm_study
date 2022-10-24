def f(index, s, e, info, lion):
    global max_ckdl
    global ans

    if index == 11:     # 마지막 인덱스까지 오면 함수 끝내기
        return
    if s == e:          # 화살 개수 다 쓰면
        a_score = 0                 # 점수 계산 시작
        l_score = 0
        for i in range(11):
            if info[i] == 0 and lion[i] == 0:
                continue
            if info[i] < lion[i]:
                l_score += (10-i)
            else:
                a_score += (10-i)

        ckdl = l_score - a_score    # 점수 계산 끝 점수 차이 저장
        if ckdl > max_ckdl:                 # 점수 차이가 여태까지 맥스 점수차이보다 크면?
            max_ckdl = ckdl                 # 정답 갱신!
            ans = lion[:]
        elif ckdl == max_ckdl:      # 점수 차이가 맥스 점수차이랑 같으면?
            for i in range(10, -1, -1):         # 끝자리부터 내려오면서
                if lion[i] == 0 and ans[i] == 0:    # 화살 개수가 둘 다 0 이 아닌 첫 i 를 찾아서
                    pass
                elif lion[i] > ans[i]:              # 새로운 정답의 화살개수가 더 크면 정답 갱신
                    ans = lion[:]
                    break
                else:                               # 그렇지 않으면 정답 갱신 안함
                    break
            return
        return
    else:                                   # f 함수는 여기서부터 동작함
        lion[index] += 1
        f(index, s+1, e, info, lion)        # 현재 index에 화살 한발 쏘고 f 함수 다시 동작
        lion[index] -= 1
        f(index+1, s, e, info, lion)        # 현재 index에 화살 안쏘고 index + 1 한 다음 f 함수 다시 동작

def solution(n, info):
    global ans          # 여기는 f 실행할때 쓸 변수들
    global max_ckdl     # 여기는 f 실행할때 쓸 변수들
    max_ckdl = 1        # 여기는 f 실행할때 쓸 변수들
    ans = [0] * 11      # 여기는 f 실행할때 쓸 변수들
    lion = [0] * 11     # 여기는 f 실행할때 쓸 변수들

    f(0,0,n,info,lion)  # 얘를 실행하면 ans가 글로벌 변수로 답이 채워짐

    if sum(ans) == 0:
        return [-1]
    else:
        return 
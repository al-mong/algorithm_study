
def shot(n, info, target, mark, peach, lion): # 남은 횟수, 피치 과녁, 쏴야할 점수, 과녁 상황, 점수들
    global answer

    # 화살이 남아있지 않거나, 목표 점수가 없을 때
    if n == 0 or target == -1:
        # 리스트를 거꾸로 된 문자열로 바꿀 것, ex) [3, 2, 1] >> '123'
        str_mark = ''
        for i in range(1, 12):
            str_mark += str(mark[-i])
        return answer.append([lion - peach, str_mark])

    # 화살을 안쏜다
    A = shot(n, info, target - 1, mark[:], peach, lion)

    # 화살을 쏜다
    mark[10 - target] += 1
    if mark[10 - target] > info[10 - target]:   # 값을 넘으면
        lion += target
        if info[10 - target]:
            peach -= target
        B = shot(n-1, info, target-1, mark[:], peach, lion)
        
    else:   # 값을 넘지 않으면
        C = shot(n-1, info, target, mark[:], peach, lion)


def solution(n, info):
    global answer

    answer = []

    peach = 0
    for i, v in enumerate(info):
        if v:
            peach += 10 - i

    result = [0 for _ in range(11)]
    shot(n, info, 10, result, peach, 0)

    answer.sort()

    if answer[-1][0] <= 0:
        return [-1]
    else:
        real = [0 for _ in range(11)]
        for i in range(11):
            real[10-i] = int(answer[-1][1][i])
        return real


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
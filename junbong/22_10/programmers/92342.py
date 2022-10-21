def solution(n, info):
    answer = [0] * 11
    result_score = 0
    
    
    def score(arr):
        nonlocal info
        result = 0
        for i in range(11):
            if info[i] == 0 and arr[i] == 0:
                continue
            if info[i] >= arr[i]:
                result -= (10 - i)
            else:
                result += (10 - i)
        return result


    def f(i, arr, arrow):
        nonlocal info, answer, result_score
        if i == 11:
            cur_score = score(arr)
            if cur_score > result_score:
                answer = arr[:]
                result_score = cur_score
            elif cur_score == result_score:
                for j in range(10, -1, -1):
                    if arr[j] > answer[j]:
                        answer = arr[:]
                        result_score = cur_score
                        break
                    elif arr[j] < answer[j]:
                        break
        else:
            if arrow - (info[i] + 1) >= 0:
                arr[i] = info[i] + 1
                f(i + 1, arr, arrow - (info[i] + 1))
                arr[i] = 0
            f(i + 1, arr, arrow)
    
    
    f(0, [0] * 11, n)
    
    rest = n - sum(answer)
    if rest >= 1:
        answer[10] += rest
    
    if result_score == 0:
        return [-1]
                
    return answer
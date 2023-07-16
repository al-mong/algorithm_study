def solution(n):
    answer = 0
    f_now = 1
    r_now = 1
    sum_now = 1
    while f_now <= n:
        if f_now == n:
            answer += 1
            break
        if sum_now <= n:
            if sum_now == n:
                answer += 1
            if r_now == n:
                sum_now -= f_now
                f_now += 1
            else:
                r_now += 1
            sum_now += r_now
        elif sum_now > n:
            sum_now -= f_now
            f_now += 1
    return answer
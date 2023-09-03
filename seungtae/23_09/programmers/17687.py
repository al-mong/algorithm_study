def change(num, n):
    # 10부터 15까지의 숫자에 대한 매핑
    digits = "0123456789ABCDEF"
    result = ""

    if num == 0:
        return "0"

    while num > 0:
        remainder = num % n
        result = digits[remainder] + result

        num = num // n

    return result


def solution(n, t, m, p):
    answer = ''
    # 0부터 1씩 올라가며 n진수로 변환할 숫자 num
    num = 0

    # 튜브의 차례를 확인하는 count
    count = 0

    while True:
        # num을 n진수로 변환
        result = change(num, n)

        # 변환된 n진수를 한글자씩 순회하며 차례를 count
        for r in result:
            count += 1

            # 튜브의 차례이면 answer에 추가
            if count == p:
                answer += r

            # 끝 차례까지 도착했다면 다시 처음 차례로
            if count == m:
                count = 0

        # 구해야하는 숫자만큼 구했다면 무한루프 종료
        if len(answer) >= t:
            break
        num += 1


    return answer[:t]

print(solution(2,4,2,1))
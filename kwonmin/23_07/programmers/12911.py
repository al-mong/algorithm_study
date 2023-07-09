# 이진수로 만든 뒤
# 앞에 0을 추가한다. (1만 있는 경우를 방지 = 빈자리 만들기)
# 규칙 1. n보다 큰 자연수여야 한다.
# 규칙 2. 1의 갯수가 같아야 한다.
# 이기 때문에, 1을 오른쪽에서 왼쪽으로 이동시켜야 한다.
# 규칙 상 0은 올 수 없다.
# ======= 풀이 ========
# 가장 낮은 1을 찾는다.
# 해당 위치로부터 왼쪽으로 이동하며 0을 찾는다.
# 두 위치를 교환한다.
# 교환된 위치로부터 아래를 정렬한다.

def solution(n):
    binary = list('0' + format(n, 'b'))     # 2진수화 시킴(1만 있는 경우를 대비해 앞에 0 추가)
    start = -1
    end = -1
    for i in range(len(binary)-1, -1, -1):  # 뒤에서부터 거슬러서 처음 나오는 1 찾기
        if binary[i] == '1':
            start = i
            break
    
    for j in range(start-1, -1, -1):        # 앞서 찾은 처음 나오는 1 위치부터 시작해서, 처음 나오는 0 찾기
        if binary[j] == '0':                # 찾았을 경우, 앞에 나온 1과 위치 바꾸기
            binary[j] = '1'
            binary[start] = '0'
            end = j
            break
    
    etc = binary[end+1:]                    # 바꾼 위치보다 작은 자리를 자르기
    etc.sort()                              # 정렬해서, 가장 작은 값으로 만들기(1010 -> 0011)
    binary = binary[:end+1] + etc           # 새로운 정답 리스트 만들기
    answer = int(''.join(b for b in binary),2) # 문자열화 시킨 후 다시 10진수화
    return answer

print(solution(15))


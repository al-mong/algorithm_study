def solution(n):
    answer = []
    arr = []
    direction = [(1, 0), (0, 1), (-1, -1)]   # 방향 설정 [down, right, up]
    
    for i in range(1, n+1):
        arr.append([0 for _ in range(1, i+1)])
    
    d_index = 0
    x, y = -1, 0
    num = 1
    
    while n != 0:

        # 한 방향동안 n 번만큼 숫자 입력
        for i in range(n):
            x += direction[d_index][0]
            y += direction[d_index][1]
            arr[x][y] = num
            num += 1

        # n 번 입력 후 방향 바꿈    
        if d_index == 2:
            d_index = 0
        else:
            d_index += 1

        # n 번 입력 후 다음 방향에서 반복할 횟수는 n-1     
        n -= 1
    
    # 2 중 배열을 순서대로 출력하기
    for i in arr:
        for j in i:
            answer.append(j)
    
    return answer
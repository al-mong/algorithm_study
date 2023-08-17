# 쭉 돌면서 4칸 확인하기
# 가능하면 지워지는 지 표시하기
# 지운 뒤를 어떻게 표시할 지가 문제.
# 구현 및 시뮬레이션...
# 뒤집는게 낫지 않을까?? 흠;;; 아닌가
# 별 차이 없으려나
# 1. 지울 수 있는 걸 순회하면서 표시한다. (visited 사용)
# 2. 지우면서 카운팅한다.
# 3. 정렬한다. <<< 이게 좀 머리에 안들어옴
# 내려가는 거라서 좀 표현이 어려운 느낌인데
# 90도 회전시키면 좀 낫지 않을까?
# 회전시키기 -> visited 체크된 거 확인 -> 없애고 0 넣기

def spin_list(rst):                 # 리스트 회전시키기
    tup = zip(*rst[::-1])           # zip으로 회전시킬 경우, tuple형태로 묶이기 때문에
    return [list(x) for x in tup]   # return하면서 list로 바꾸는 과정이 필요

def solution(m, n, board):          # m : x축, n : y축. 여기서는 회전시키므로 바꿔서 사용
    field = spin_list(board)
    answer = 0
    while True:
        flag = False
        visited = [[0]*m for _ in range(n)]     # 같은 블록이 여러 2x2에 포함될 수 있으므로 바로 변환하면 안됨 -> 변환할 좌표 리스트
        for i in range(n-1):
            for j in range(m-1):
                if field[i+1][j+1] != 0 and field[i][j] == field[i+1][j] == field[i][j+1] == field[i+1][j+1]:
                    # 4개가 같은 지 확인. 이것도 for문처리하고 싶었지만, 그러려면 for문이 4개가 더 필요해서 수작업
                    visited[i][j] = 1
                    visited[i+1][j] = 1
                    visited[i][j+1] = 1
                    visited[i+1][j+1] = 1
                    flag = True
        
        if not flag:                # 바뀐 게 없다면 : 아래의 과정이 필요가 없으니까 종료
            break
        
        for i in range(n):
            for j in range(m):
                if visited[i][j]:       # 바뀌었다면
                    field[i][j] = -1    # -1로 (일단) 바꿔주고
                    field[i].append(0)  # 뒤에 0을 집어넣음(리스트의 전체 길이 유지)
                    answer += 1

            field[i] = [x for x in field[i] if x != -1] # -1을 없애기
        

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
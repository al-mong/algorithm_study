# 갈 수 있는지 아닌지 먼저 판별
# 그 뒤 경로 만들면 됨
# bfs로 하는데, 거리 체크해서 백트래킹 하면 될듯
# x,y,r,c -1씩 해줘야 함 (유의)



def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    # drlu 순 = 아래 오른쪽 왼쪽 위
    drc = [(1,0,"d"),(0,-1,"l"),(0,1,"r"),(-1,0,"u")]

    def DFS(stt_x, stt_y, r, c, k, root):
        nonlocal answer
        nonlocal n
        nonlocal m
        거리 = abs(r-stt_x)+abs(c-stt_y)

        if 거리 > k or (k-거리)%2 or k < 0 or answer != 'impossible':
            return
        if stt_x == r and stt_y == c and k == 0:
            answer = root
            return
        
        for rx, ry, d in drc:
            nx = stt_x + rx 
            ny = stt_y + ry
            if nx <= 0 or nx > n or ny <= 0 or ny > m:
                continue
            DFS(nx, ny, r, c, k-1, root+d)

    DFS(x, y, r, c, k, "")

    return answer

print(solution(3,4,2,3,3,1,5))
print(solution(2,2,1,1,2,2,2))
print(solution(3,3,1,2,3,3,4))
import sys
sys.setrecursionlimit(100000000)
def hey(x,y):
    nums[y][x] = 0
    d = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]    # 대각선으로는 움직일 수 없음
    for dd in d:
        ny = y + dd[0]
        nx = x + dd[1]
        if w > nx >= 0 and h > ny >= 0 and nums[ny][nx] == 1:      #범위안에 있고 연결된 땅이 있으면 
            hey(nx, ny)                                            #다음 땅으로 이동

while True:
    w, h =  map(int,(input().split()))
    if w == 0 and h == 0:                                          #멈추라는 신호 들어오면 멈춰~~
        break
    nums = [list(map(int, input().split()))+[0] for _ in range(h)]
    
    ans = 0
    for j in range(h):
        for i in range(w):
            if nums[j][i] == 1:                                    # 땅있으면 고고
                hey(i,j)
                ans += 1                                           #이미 갔던 땅은 0이라서 안가고 땅 개수나옴
    print(ans)
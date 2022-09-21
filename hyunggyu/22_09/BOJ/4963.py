# 4963 섬의 개수
# 땅과 바다
# 가로 세로 대각선으로 연결되면 걸어갈수 있다.
def search():
    while q:
        i, j = q.pop()
        for di,dj in [[1,0],[-1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]:
            ni = i + di
            nj = j + dj
            if ni<0 or nj< 0 or ni>= w or nj>= h:
                pass
            else:
                if land[nj][ni] == 1 and visited[nj][ni] == 0:
                    q.append((ni,nj))
                    visited[nj][ni] = 1

# 땅 1 바다 0
# 마지막 줄에는 00준다.
while True:
    w, h = map(int, input().split()) # 50이하
    if w == 0 and h == 0:
        break
    else:
        land = [list(map(int, input().split())) for _ in range(h)]
        # visited 방문시 1 안하면 0
        visited = [[0]*w for _ in range(h)]
        # 섬의 개수 출력
        cnt = 0
        q = []
        for j in range(h):
            for i in range(w):
                if land[j][i] == 1 and visited[j][i] == 0:
                    visited[j][i] = 1
                    q.append((i,j))
                    search()
                    cnt += 1
        print(cnt)
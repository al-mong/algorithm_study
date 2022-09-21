# 양 한마리... 양 두마리...
# 양은 # .은 풀 #2개 붙으면 양무리
from collections import deque
def search():
    while q:
        i,j = q.popleft()
        for di, dj in [[1,0],[0,-1],[-1,0],[0,1]]:
            nj = j + dj
            ni = i + di
            if nj<0 or nj>= h or ni <0 or ni >=w:
                pass
            elif grassland[nj][ni] == '#' and not visited[nj][ni]:
                q.append((ni,nj))
                visited[nj][ni] = 1                                    # bfs 로 목장 확인


T = int(input())
for t in range(T):
    q = deque()
    h, w = map(int, input().split())
    visited = [[0]*w for _ in range(h)]
    grassland = [list(input()) for _ in range(h)]
    cnt = 0
    for j in range(h):
        for i in range(w):
            if not visited[j][i] and grassland[j][i] == '#':            # 확인 안된 지역있으면 cnt +1
                q.append((i,j))
                visited[j][i] = 1
                cnt += 1
                search()
    print(cnt)
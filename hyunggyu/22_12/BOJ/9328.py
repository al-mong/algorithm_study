# 일부열쇠 들고있고, 일부는 바닥에 위치
# 상하좌우 이동 가능 훔칠수 있는 문서개수
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    h, w = map(int, input().split())
    # 지도의 높이와 너비 2~100
    graph = [['*']*(w+2)] + [['*']+list(input().strip())+['*'] for _ in range(h)] +[['*']*(w+2)]
    # . 빈공간 * 벽 $ 문서 대문자는 문 소문자는 열쇠
    # str은 할당할수 없으므로 숫자로 변경
    graph2 = [[0]*(w+2) for _ in range(h+2)]
    for j in range(h+2):
        for i in range(w+2):
            if graph[j][i] == '.':
                graph2[j][i] = 1
            elif graph[j][i] == '*':
                continue
            elif graph[j][i] == '$':
                graph2[j][i] = 2
            else:
                graph2[j][i] = ord(graph[j][i])

    get = list(input().rstrip()) # 키 97~122 문 65~90
    key = [0]*26 # 키 최신화
    moon = [0]*26
    if get[0] != '0': # 열쇠개수가 0이 아니면 key등록
        for i in range(len(get)):
            num = ord(get[i])-97
            key[num] = 1
    # bfs 를 통해서 검색 + 만약 alpha라면 위치 저장해두고 나중에 처리
    que = deque()
    for j in range(h+2):
        for i in range(w+2):
            if j == 0 or i == 0 or j == h+1 or i == w+1:
                que.append((j,i))
    result = 0
    while que:
        j,i = que.popleft()
        for dj,di in [(-1,0),(1,0),(0,1),(0,-1)]:
            nj = j + dj
            ni = i + di
            if nj < 0 or ni < 0 or nj >= h+2 or ni >= w+2: # 범위를 벗어나면 아웃
                continue
            if graph2[nj][ni] == 0:
                continue
            elif graph2[nj][ni] == 1:
                que.append((nj,ni))
                # 이동했다면 전 장소 벽치기(visited)
                graph2[nj][ni] = 0
            elif graph2[nj][ni] == 2:
                result += 1
                que.append((nj,ni))
                graph2[nj][ni] = 0
            # 알파벳이라면
            else:
                ck = graph2[nj][ni]
                if ck >= 97:
                    # 키라면
                    key[ck-97] = 1
                    que.append((nj,ni))
                    graph2[nj][ni] = 0
                    if moon[ck-97] != 0:
                        # 키를 먹었을 때 문을 들린 곳이라면
                        nj,ni = moon[ck-97]
                        que.append((nj,ni))
                        graph2[nj][ni] = 0
                else:
                    # 문이라면
                    if key[ck-65] == 1:
                        # 키가 있다면
                        que.append((nj,ni))
                        graph2[nj][ni] = 0
                    else:
                        # 키가 없다면
                        if moon[ck-65] == 0:
                            moon[ck-65] = (nj,ni)
                        else:
                            moon[ck-65].append((nj,ni)) # -> 리스트형식으로 바꿔서 키를 넣어 키가 생기면 모두 비교하게 바꾸자
                        continue
    # 키 -> 문 : 바로 열림
    # 문 -> 키 : 키가 문을 확인하고 그 장소로 이동
    # 문제 한개의 키에 문이 여러개 일수 있다....후....
    print(result)
# 초기아이디어
# 대문자알파벳을 만났을 경우에도 큐에 넣어둠
# 자물쇠큐를 따로 만들어둘까?
# 그래서 큐가 비었을 경우 자물쇠큐도 확인함
# 자물쇠큐 확인하면서 열 수 있는 애가 있으면, 해당 위치 큐에 추가해줌
# (자물쇠, x좌표, y좌표) 를 넣어두면 될 것 같은데
# 순회를 어떻게 하느냐가 관건인듯
# defaultdict로 해봐도 될수도?
from string import ascii_lowercase, ascii_uppercase # 알파벳 리스트로 쓸 로우케이스랑 어퍼케이스
from collections import deque # BFS 사용
from collections import defaultdict # 아직 열지 못한 문 넣어둘 defaultdict

def BFS():
    global doc_cnt

    while que:
        x, y = que.popleft()

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x + dx, y + dy

            if nx >= N or nx < 0 or ny >= M or ny < 0 or field[nx][ny] == '*':
                continue

            if field[nx][ny] == '.': # 갈 수 있는 길일 경우, 지나가고 방문처리
                field[nx][ny] = '*'
                que.append((nx,ny))
            
            elif field[nx][ny] == '$': # 문서 획득했을 경우 카운트 올려주고 방문처리
                doc_cnt += 1
                field[nx][ny] = '*'
                que.append((nx,ny))
            
            elif field[nx][ny] in keys: # 열쇠일 경우
                k = field[nx][ny] # 알아보기 쉽게 key 꺼내기
                if keys[k] == 1:    # 만약 이미 열쇠가 있을 경우는, 해당 방에 방문했을 경우에도 모두 열었을 것.
                                    # 그러므로 그냥 방문처리 하면 됨
                    field[nx][ny] = '*'
                    que.append((nx,ny))
                else:               # 만약 열쇠가 없었을 경우에는, 열지못한 문들이 door에 남아있을 가능성이 있음
                                    # 그래서 새로운 열쇠를 획득했을 경우, 해당 문이 있는지를 확인하고 해당 문 좌표를 큐에 넣어줌
                    keys[k] = 1
                    field[nx][ny] = '*'
                    if k in door:
                        while door[k]:
                            nnx, nny = door[k].pop()
                            field[nnx][nny] = '*'
                            que.append((nnx,nny))
                    que.append((nx,ny))
            
            else:                           # 만약 잠긴 문의 경우
                k = field[nx][ny].lower()   # 맞는 열쇠를 찾기 위해 소문자로 변경
                if keys[k] == 1:            # 맞는 열쇠가 있을 경우에는 방문처리
                    field[nx][ny] = '*'
                    que.append((nx,ny))
                else:                       # 없을 경우에는 door 딕셔너리에 추가하기
                    door[k].append((nx,ny))
    
    print(doc_cnt)  # 순회완료






lock_list = list(ascii_uppercase)   # 알파벳 대문자 저장해두는 리스트

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    doc_cnt = 0
    field = [list(input()) for _ in range(N)]
    que = deque()                   # 방문할 지점들 담아둘 큐
    door = defaultdict(list)        # 열지못한 문들 담아둘 디폴트딕트
    keys = {}                       # 알파벳 소문자 저장해두는 딕셔너리
    for alp in ascii_lowercase:
        keys[alp] = 0

    default_keys = list(input())    # 처음 가진 열쇠들
    if default_keys[0] != '0':      # 순회하면서 열쇠꾸러미에 담아두기
        for k in default_keys:
            keys[k] = 1

    for i in range(N):              # 모서리 돌면서 큐에 좌표넣기. BFS에서 처리하는 과정과 동일
        for j in range(M):
            if i == 0 or j == 0 or i == N-1 or j == M-1:
                if field[i][j] == '.':
                    que.append((i,j))
                    field[i][j] = '*'
                elif field[i][j] == '$':
                    doc_cnt += 1
                    field[i][j] = '*'
                    que.append((i,j))
                elif field[i][j] in keys:
                    k = field[i][j]
                    if keys[k] == 1:
                        field[i][j] = '*'
                        que.append((i,j))
                    else:
                        keys[k] = 1
                        field[i][j] = '.'
                        if k in door:
                            while door[k]:
                                nnx, nny = door[k].pop()
                                field[nnx][nny] = '*'
                                que.append((nnx,nny))
                        que.append((i,j))
                elif field[i][j] in lock_list:
                    k = field[i][j].lower()
                    if keys[k] == 1:
                        field[i][j] = '*'
                        que.append((i,j))
                    else:
                        door[k].append((i,j))

    BFS()

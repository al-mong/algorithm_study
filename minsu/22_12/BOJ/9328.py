from collections import deque
from pprint import pprint

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(x,y):
    q = deque()
    visited = [[0]*(w+2) for _ in range(h+2)]
    q.append([x, y])
    visited[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            ni = x + di[i]
            nj = x + dj[i]
            if 0 <= ni < h + 2 and 0 <= nj < w + 2:
                print(ni, nj)
                if not visited[ni][nj]:
                    if case[ni][nj] == '.':                             # .이면
                        visited[ni][nj] = 1
                        pprint(visited)
                        q.append([ni, nj])

                    elif case[ni][nj].islower():                        # 소문자이면
                        door[ord(case[ni][nj]) - ord('a')] = 1          # 키 리스트에 1을 더하고
                        q = deque()                                     # q , visited 초기화
                        visited = [[0]*(w+2) for _ in range(h+2)]
                        case[ni][nj] = '.'
                        q.append([ni, nj])

                    elif case[ni][nj].isupper():                        # 대문자이면
                        if door[ord(case[ni][nj]) - ord('A')]:          # 키(소문자)가 있는지 확인
                            visited[ni][nj] = 1
                            case[ni][nj] = '.'
                            q.append([ni, nj])

                    elif case[ni][nj] == '$':                          # $ 이면
                        visited[ni][nj] = 1
                        cnt += 1
                        case[ni][nj] = '.'
                        q.append([ni, nj])

    return cnt

# 맵에 패딩 넣기
def new_map():
    for i in case:
        i.insert(0, '.')
        i.append('.')
    case.insert(0, ['.']*(w+2))
    case.append(['.'] * (w + 2))

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    case = []
    for _ in range(h):
        case.append(list(input()))
    key = list(input())
    door = [0]*26

    # 받은 키를 키 리스트에 넣기
    for k in key:
        if k != '0':
            door[ord(k) - ord('a')] = 1

    # 미리 받은 키로 문 열기
    for i in range(h):
        for j in range(w):
            if ord('A') <= ord(case[i][j]) <= ord('Z'):
                if door[ord(case[i][j]) - ord('A')]:
                    case[i][j] = '.'

    new_map()
    print(bfs(0,0))
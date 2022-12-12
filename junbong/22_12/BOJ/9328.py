import sys; input = sys.stdin.readline
from collections import deque, defaultdict


def sol(i, j):
    global result
    q = deque([(i, j)])

    while q:
        v = q.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = v[0] + di, v[1] + dj

            if ni < 0 or ni >= h or nj < 0 or nj >= w or building[ni][nj] == '*':
                continue
            
            char = building[ni][nj]
            building[ni][nj] = '*'  # 방문 체크
             
            if char == '$':  # 다음 탐색 위치가 문서라면
                result += 1
            elif 65 <= ord(char) <= 90:  # 다음 탐색 위치가 문이라면
                if not char.lower() in keys:  # 열쇠가 없으면 막힘
                    blocked_doors[char].append((ni, nj))  # 막혔던 위치 저장
                    continue  # q에 append되면 안됨!
            elif 97 <= ord(char) <= 122:  # 다음 탐색 위치가 열쇠라면
                if not char in keys:
                    keys.add(char)  # 열쇠 목록에 저장
                    for blocked_door in blocked_doors[char.upper()]:  # 막혔던 곳 다시 가보기
                        q.append(blocked_door)
            
            q.append((ni, nj))


for T in range(int(input().rstrip())):
    h, w = map(int, input().split())  # 행, 열
    building = [list(input().rstrip()) for _ in range(h)]  # 빌딩
    keys_input = input().rstrip()  # 열쇠 입력
    keys = set()  # 열쇠
    if keys_input != '0':
        for key in keys_input:
            keys.add(key)
    result = 0
    
    starts = deque()  # 시작 위치 저장용 리스트
    blocked_doors = defaultdict(list)  # 막혔던 위치 저장용 딕셔너리

    for i in range(h):
        for j in range(w):
            char = building[i][j]
            
            # 시작 위치 넣어주기
            if i == 0 or i == h - 1:  # 첫 행과 마지막 행에서
                building[i][j] = '*'  # 시작점 방문 체크
                if char == '$':
                    result += 1
                    starts.append((i, j))
                elif 65 <= ord(char) <= 90:
                    blocked_doors[char].append((i, j))
                elif 97 <= ord(char) <= 122:
                    keys.add(char)
                    starts.append((i, j))
                elif char == '.':
                    starts.append((i, j))
            else:
                if j == 0 or j == w - 1:
                    building[i][j] = '*'
                    if char == '$':
                        result += 1
                        starts.append((i, j))
                    elif 65 <= ord(char) <= 90:
                        blocked_doors[char].append((i, j))
                    elif 97 <= ord(char) <= 122:
                        keys.add(char)
                        starts.append((i, j))
                    elif char == '.':
                        starts.append((i, j))

    # 시작 테두리에서 주웠던 열쇠들에 맞는 문 열어주기
    for key in keys:
        for blocked_door in blocked_doors[key.upper()]:  # 테두리에서 막혔던 문 시작 위치에 넣기
            starts.append(blocked_door)

    for start in starts:
        sol(start[0], start[1])

    print(result)

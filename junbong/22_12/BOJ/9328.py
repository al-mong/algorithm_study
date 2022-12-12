# 221212

'''
PyPy3 - 2080 ms

입력받을 때 문의 위치들을 다 저장해놓고, 열쇠를 얻었을 때 열 수 있는 문 다 열기
테두리에 있는 문이라면 시작 위치에 넣어주기

열쇠의 개수가 변함이 없으면 갈 수 있는 위치가 같다는 뜻이므로
bfs를 한 사이클 돌았을 때 열쇠의 개수가 변함이 없으면 끝낸다.
'''

import sys; input = sys.stdin.readline
from collections import deque, defaultdict


def sol(i, j):
    global result
    q = deque([(i, j)])
    visited = [[0 for _ in range(w)] for _ in range(h)]
    visited[i][j] = 1

    while q:
        v = q.popleft()
        # print(v)
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = v[0] + di, v[1] + dj

            if ni < 0 or ni >= h or nj < 0 or nj >= w or building[ni][nj] == '*' or visited[ni][nj] or 65 <= ord(building[ni][nj]) <= 90:
                # 다음 탐색 위치가 문이라면 볼 필요가 없다.
                # 어짜피 열쇠를 얻을 때마다 열 수 있는 문은 다 열어놓을 것
                continue
            
            char = building[ni][nj]
            visited[ni][nj] = 1  # 방문 체크
             
            if char == '$':  # 다음 탐색 위치가 문서라면
                result += 1
                building[ni][nj] = '.'
            elif 97 <= ord(char) <= 122:  # 다음 탐색 위치가 열쇠라면
                if not char in keys:
                    keys.add(char)  # 열쇠 목록에 저장
                    for door_pos in doors[char.upper()]:  
                        building[door_pos[0]][door_pos[1]] = '.'  # 해당 열쇠로 열 수 있는 문 다 열어놓기
                        # 테두리 위치의 문을 열었으면 시작 포인트에 추가
                        if door_pos[0] == 0 or door_pos[0] == h - 1 or door_pos[1] == 0 or door_pos[1] == w - 1:  
                            starts.append((door_pos[0], door_pos[1]))
            
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
    
    starts = []  # 시작 위치 저장용 리스트
    doors = defaultdict(list)  # 문 위치 저장용 딕셔너리
    for i in range(h):
        for j in range(w):
            # 문 위치 저장해놓기
            if 65 <= ord(building[i][j]) <= 90:
                if building[i][j].lower() in keys:
                    building[i][j] = '.'
                else:
                    doors[building[i][j]].append((i, j))
            
            # 초기에 시작 위치 넣어주기
            if i == 0 or i == h - 1:
                char = building[i][j]
                if char == '*' or 65 <= ord(char) <= 90:  # 이미 열쇠가 있는 문들은 열어놨으므로, 문이 나오면 넘어감
                    continue
                starts.append((i, j))
                if char == '$':
                    result += 1
                elif 97 <= ord(char) <= 122:
                    keys.add(char)
                building[i][j] = '.'  # 문서든 열쇠든, 주웠으니까 빈 칸으로
        
        # 초기에 시작 위치 넣어주기
        if i != 0 and i != h - 1:
            for j in [0, w - 1]:
                char = building[i][j]
                if char == '*' or 65 <= ord(char) <= 90:
                    continue
                starts.append((i, j))
                if char == '$':
                    result += 1
                elif 97 <= ord(char) <= 122:
                    keys.add(char)
                building[i][j] = '.'
    
    # print(doors)
    # print(starts)

    for key in keys:
        for door_pos in doors[key.upper()]:  
            building[door_pos[0]][door_pos[1]] = '.'  # 해당 열쇠로 열 수 있는 문 다 열어놓기
            # 테두리 위치의 문을 열었으면 시작 포인트에 추가
            if door_pos[0] == 0 or door_pos[0] == h - 1 or door_pos[1] == 0 or door_pos[1] == w - 1:  
                starts.append((door_pos[0], door_pos[1]))

    num_of_key = len(keys)
    while True:
        for start in starts:
            sol(start[0], start[1])

        if num_of_key == len(keys):  
            break
        else:
            num_of_key = len(keys)

    print(result)

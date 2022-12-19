import sys
input = sys.stdin.readline
from collections import deque

T = int(input().rstrip())
for t in range(T):
    V, E = map(int,input().split())
    # V  정점의 개수(1~V), E 간선의 개수
    visited = [0]*(V+1)
    team = [[] for _ in range(V+1)]

    # 루트를 중심으로 자식 체크
    for _ in range(E):
        i, j = map(int,input().split())
        team[i].append(j)
        team[j].append(i)
    
    # team을 1, -1로 나눠서 같을 경우 끝내기
    flag = True
    # 1은 1팀으로 기준 정하기
    visited[1] = 1
    q = deque([1])
    def BFS():
        global visited
        global flag
        global q
        while q:
            # BFS
            k = q.popleft()

            # flag로 중단 조건 확인
            if flag == False:
                break

            # a = another team
            for a in team[k]:
                if visited[a] == 0:
                    q.append(a)
                    visited[a] = -visited[k]
                elif visited[a] == visited[k]:
                    flag = False
    
    # 따로 돌고 있는 루틴이 있을수 있으니깐
    for i in range(1,V+1):
        if flag == False:
            break
        if visited[i] == 0:
            q.append(i)
            # 초기값의 경우 새로운 루틴의 시작이니깐 1
            visited[i] = 1
            BFS()

    # 결과값 출력
    if flag == False:
        print("NO")
    else:
        print("YES")
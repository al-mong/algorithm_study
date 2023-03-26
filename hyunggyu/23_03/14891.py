# 톱니바퀴 왼쪽부터 1234번
# k번 회전시킬때 한칸을 기준으로(시계, 반시계)
# 돌리기전 서로 맡닿은 극에 따라 극이 다르면 반대방향으로 회전 같으면 정지 
import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

# 톱니바퀴의 상태
# 12시부터 차례대로 8개 배열; N극은 0, S극은 1
# 2와 6이 비교
status = list(deque(input().rstrip()) for i in range(4))

# 회전 시키기
def gogo(n, dir):
    status[n].rotate(dir)
    # 1이면 시계, -1이면 반시계
    
def change(n, dir):
    # 제외처리
    
    # 방문했다면
    if visited[n]:
        return
    # 방문처리
    visited[n] = 1
    v_rotate[n] = dir
    # 전에가 회전하지 않는다면 그냥 끝내기
    if dir == 0:
        return
    
    # 회전
    right =  status[n][2]
    left = status[n][6]
    if n == 3:
        if left == status[n-1][2]:
            change(n-1,0)
        else:
            change(n-1,-dir)
    elif n == 0:
        if right == status[n+1][6]:
            change(n+1,0)
        else:
            change(n+1,-dir)
    else:
        if left == status[n-1][2]:
            change(n-1,0)
        else:
            change(n-1,-dir)
        if right == status[n+1][6]:
            change(n+1,0)
        else:
            change(n+1,-dir)


k = int(input())
for _ in range(k):
    n, dir = map(int, input().split())
    n -= 1
    # 초기화
    visited = [0,0,0,0]
    v_rotate = [0,0,0,0]
    change(n, dir)
    # 회전 방향을 정하고 회전시키기
    # print(v_rotate)
    for i in range(4):
        if v_rotate[i] != 0:
            gogo(i, v_rotate[i])
result = 0
for i in range(4):
    result += int(status[i][0]) * (2 **i)
print( result)
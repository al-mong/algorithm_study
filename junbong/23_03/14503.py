# 230306

'''
방문(청소) 체크를 1로 해버려서, 이미 청소한 벽이 아닌 곳으로 후진을 못함
-1로 한 뒤 해결
'''

import sys
input = sys.stdin.readline

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sol(i, j, d):
    global result

    if room[i][j] == 0:
        room[i][j] = -1  # 방문(청소) 체크
        result += 1

    for k in range(1, 5):  # 반시계 방향으로 90도 먼저 회전하므로 0부터가 아닌 1부터 4까지 빼줌
        ni, nj = i + dir[(d - k) % 4][0], j + dir[(d - k) % 4][1]
        # 반시계 방향으로 회전하다가 앞이 청소되지 않은 빈 칸인 경우
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0:
            sol(ni, nj, (d - k) % 4)
            break  # dfs가 아니므로 break로 for문을 나와줘야 한다
    # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        ni, nj = i - dir[d][0], j - dir[d][1]  # 후진할 위치
        # 후진 위치가 벽이 아닌 경우
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0 or room[ni][nj] == -1:
            sol(ni, nj, d)
        # 벽인 경우, 범위를 벗어난 경우도 벽임
        else:
            return


N, M = map(int, input().split())
si, sj, sd = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
result = 0

sol(si, sj, sd)

print(result)

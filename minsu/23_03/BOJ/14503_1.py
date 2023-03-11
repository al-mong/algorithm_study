import sys
input = sys.stdin.readline

result = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def func(r, c, d):
    global result

    while True:
        if arr[r][c] == 0:
            result += 1
            arr[r][c] = 2

        # 상하좌우 빈칸 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if arr[nr][nc] == 0:
                break

        # 상하좌우에 빈칸이 안나오고 for문이 끝나면 실행
        # 후진 이동
        else:
            if d == 0:
                r += 1
            elif d == 1:
                c -= 1
            elif d == 2:
                r -= 1
            else:
                c += 1

            if arr[r][c] != 1:  # 벽 안쪽이라 벽 벗어나는 거 생각 안해도 될듯
                continue
            else:
                break

        # 상하좌우에 빈칸이 있으면
        # 반시계 90도
        d -= 1
        if d < 0:
            d = 3
        nr = r + dr[d]
        nc = c + dc[d]

        if arr[nr][nc] == 0:
            r = nr
            c = nc
            continue

func(r, c, d)
print(result)


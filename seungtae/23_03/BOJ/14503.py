import sys
input = sys.stdin.readline

def f(r, c, d):
    global total
    
    # 청소되지 않은 방이면 청소 count + 1
    if not visited[r][c]:
        total += 1
        visited[r][c] = 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if isClean(r, c):
        if d == 0:
            if r+1 != n and arr[r+1][c] != 1:
                f(r+1, c, d)
        elif d == 1:
            if c - 1 >= 0 and arr[r][c-1] != 1:
                f(r, c-1, d)
        elif d == 2:
            if r - 1 >= 0 and arr[r-1][c] != 1:
                f(r-1, c, d)
        elif d == 3:
            if c + 1 != m and arr[r][c+1] != 1:
                f(r, c+1, d)
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        # 북
        if d == 0:
            if c-1 >= 0 and not arr[r][c-1] and visited[r][c-1] != 1:
                f(r, c-1, 3)
            else:
                f(r, c, 3)

        # 서
        if d == 3:
            if r+1 < n and not arr[r+1][c] and visited[r+1][c] != 1:
                f(r+1, c, 2)
            else:
                f(r, c, 2)

        # 남
        if d == 2:
            if c+1 < m and not arr[r][c+1] and visited[r][c+1] != 1:
                f(r, c+1, 1)
            else:
                f(r, c, 1)

        # 동
        if d == 1:
            if r-1 >= 0 and not arr[r-1][c] and visited[r-1][c] != 1:
                f(r-1, c, 0)
            else:
                f(r, c, 0)


def isClean(r, c):
    if r - 1 > 0 and not arr[r-1][c] and not visited[r - 1][c]:
        return False
    if r + 1 < n and not arr[r+1][c] and not visited[r + 1][c]:
        return False
    if c - 1 > 0 and not arr[r][c-1] and not visited[r][c - 1]:
        return False
    if c + 1 > 0 and not arr[r][c+1] and not visited[r][c + 1]:
        return False
    return True



n, m = map(int, input().split())
sr, sc, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

total = 0

f(sr, sc, d)

print(total)
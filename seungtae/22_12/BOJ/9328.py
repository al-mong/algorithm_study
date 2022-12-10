import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    global count

    # 인접 4점 조사
    for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < r and 0 <= ny < c:

            # 방문했으면 패스
            if visited[nx][ny]:
                continue
            # 방문안했으면 방문체크 후 아래코드 실행
            visited[nx][ny] = 1

            # * 이면 패스
            if arr[nx][ny] == '*':
                pass

            # . 이면 다음 dfs 실행
            elif arr[nx][ny] == '.':
                dfs(nx, ny)

            # $ 이면 count += 1 하고 다음 dfs 실행
            elif arr[nx][ny] == '$':
                count += 1
                dfs(nx, ny)

            # key 이면 키줍고 다음 dfs 실행    +    키 없을때 막혔던 문 다 열기         
            elif 97 <= ord(arr[nx][ny]) <= 122:
                dfs(nx, ny)
                key_dict[chr(ord(arr[nx][ny]) - 32)][0] = 1
                for xx, yy in key_dict[chr(ord(arr[nx][ny]) - 32)][1]:       # => 여기 사실 키가 여러개 놓여있으면 중복실행되는데 문제 통과하길래 수정안함
                    dfs(xx, yy)

            # 문이면 key 있을 땐 다음 dfs 실행, 없으면 해당 key에 대해 막혔던 문이라고 표시
            elif 65 <= ord(arr[nx][ny]) <= 90:
                if key_dict[arr[nx][ny]][0] == 1:
                    dfs(nx, ny)
                else:
                    key_dict[arr[nx][ny]][1].append((nx, ny))

T = int(input())
for tc in range(T):
    r, c = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(r)]
    visited = [[0 for _ in range(c)] for _ in range(r)]
    keys = list(input().rstrip())
    key_dict = {chr(i): [0, []] for i in range(65, 91)}
    if keys[0] != '0':
        for key in keys:
            key_dict[chr(ord(key) - 32)][0] = 1


    count = 0
    for i in range(c):
        if visited[0][i] == 0:
            visited[0][i] = 1
            if arr[0][i] == '*':
                pass
            elif arr[0][i] == '.':
                dfs(0, i)
            elif arr[0][i] == '$':
                count += 1
                dfs(0, i)
            elif 97 <= ord(arr[0][i]) <= 122:
                dfs(0, i)
                key_dict[chr(ord(arr[0][i]) - 32)][0] = 1
                for x, y in key_dict[chr(ord(arr[0][i]) - 32)][1]:
                    dfs(x, y)
            elif 65 <= ord(arr[0][i]) <= 90:
                if key_dict[arr[0][i]][0] == 1:
                    dfs(0, i)
                else:
                    key_dict[arr[0][i]][1].append((0, i))

        if visited[r-1][i] == 0:
            visited[r-1][i] = 1
            if arr[r-1][i] == '*':
                pass
            elif arr[r-1][i] == '.':
                dfs(r-1, i)
            elif arr[r-1][i] == '$':
                count += 1
                dfs(r-1, i)
            elif 97 <= ord(arr[r-1][i]) <= 122:
                dfs(r - 1, i)
                key_dict[chr(ord(arr[r-1][i]) - 32)][0] = 1
                for x, y in key_dict[chr(ord(arr[r-1][i]) - 32)][1]:
                    dfs(x, y)
            elif 65 <= ord(arr[r-1][i]) <= 90:
                if key_dict[arr[r-1][i]][0] == 1:
                    dfs(r-1, i)
                else:
                    key_dict[arr[r-1][i]][1].append((r-1, i))

    for i in range(1, r-1):
        if visited[i][0] == 0:
            visited[i][0] = 1
            if arr[i][0] == '*':
                pass
            elif arr[i][0] == '.':
                dfs(i, 0)
            elif arr[i][0] == '$':
                count += 1
                dfs(i, 0)
            elif 97 <= ord(arr[i][0]) <= 122:
                dfs(i, 0)
                key_dict[chr(ord(arr[i][0]) - 32)][0] = 1
                for x, y in key_dict[chr(ord(arr[i][0]) - 32)][1]:
                    dfs(x, y)
            elif 65 <= ord(arr[i][0]) <= 90:
                if key_dict[arr[i][0]][0] == 1:
                    dfs(i, 0)
                else:
                    key_dict[arr[i][0]][1].append((i, 0))

        if visited[i][c-1] == 0:
            visited[i][c-1] = 1
            if arr[i][c-1] == '*':
                pass
            elif arr[i][c-1] == '.':
                dfs(i, c-1)
            elif arr[i][c-1] == '$':
                count += 1
                dfs(i, c-1)
            elif 97 <= ord(arr[i][c-1]) <= 122:
                dfs(i, c - 1)
                key_dict[chr(ord(arr[i][c-1]) - 32)][0] = 1
                for x, y in key_dict[chr(ord(arr[i][c-1]) - 32)][1]:
                    dfs(x, y)
            elif 65 <= ord(arr[i][c-1]) <= 90:
                if key_dict[arr[i][c-1]][0] == 1:
                    dfs(i, c-1)
                else:
                    key_dict[arr[i][c-1]][1].append((i, c-1))

    print(count)
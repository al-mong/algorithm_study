def dfs(depth, idx):
    global min_diff
    if depth == (N//2):
        start, link = 0,0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    start += (arr[i][j] + arr[j][i])
                elif not visited[i] and not visited[j]:
                    link += (arr[i][j] + arr[j][i])

        min_diff = min(min_diff, abs(start - link))

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth +1, i +1)
            visited[i] = False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_diff = 999999
visited = [False] *(N+1)

dfs(0, 0)
print(min_diff)

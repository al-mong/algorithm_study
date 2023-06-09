import sys
sys.setrecursionlimit(10000)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dc = ['d', 'l', 'r', 'u']  # 알파벳 오름차순
answer = ''


def dfs(n, m, r, c, k, px, py, cnt, record):
    global answer

    # 처음엔 solution의 dis관련 if문에서 다 걸러주니 필요없다고 생각 -> 먼 방향으로 갔을 때 유효한지 검사 필요
    # 목적지와 먼 방향으로 갔는데 이동 횟수가 넉넉하지 않은 경우
    # 이미 answer가 있는 경우, answer가 한번만 정해지면 다른 건 볼 필요 없음(알파벳 순)
    if cnt + abs(px - r) + abs(py - c) > k or answer:
        return

    if cnt == k and px == r and py == c:
        answer = record
        return

    for i in range(4):
        nx, ny = px + dx[i], py + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m:
            dfs(n, m, r, c, k, nx, ny, cnt + 1, record + dc[i])


def solution(n, m, x, y, r, c, k):
    dis = abs(x - r) + abs(y - c)

    # k가 최소 이동 거리보다 크거나, 목적지까지 이동 후 왕복으로 k번을 채울 수 없으면 impossible
    if dis > k or (k - dis) % 2:
        return 'impossible'

    dfs(n, m, r, c, k, x, y, 0, '')

    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))

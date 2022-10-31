import heapq

def solution(n, paths, gates, summits):

    def find_summit():
        nonlocal minIntensity, summit

        maxInten = 0
        while q:
            # 힙큐에서 intensity가 가장 작은 원소를 하나 pop 하기
            intensity, now = heapq.heappop(q)

            # 다른 게이트나 이미 지나간 쉼터일때
            if gates_dic[now] or visited[now]:
                continue

            # 위에서 걸러지지 않으면 정상적인 로직 처리 - 1. 방문체크. 2. inten 갱신. 3. 루트 추가
            visited[now] = True
            maxInten = max(maxInten, intensity)
            route.append(now)

            # 가지치기
            if maxInten > minIntensity:
                return

            # 봉우리를 찾았을 때
            if now in summits:
                if maxInten < minIntensity:
                    minIntensity = maxInten
                    summit = now
                elif maxInten == minIntensity:
                    summit = min(summit, now)
                return

            # 위의 경우가 아닐 때
            for inten, nextt in adj[now]:
                if gates_dic[nextt] or visited[nextt]:
                    continue
                heapq.heappush(q, (inten, nextt))


    # 전역 변수로 사용할 거
    minIntensity = 1e10
    summit = 0

    # 게이트, 봉우리 정보 저장
    gates_dic = {i: False for i in range(1, n+1)}
    for u in gates:
        gates_dic[u] = True

    summits = set(summits)

    # 경로 정보 저장
    adj = {i: [] for i in range(1, n+1)}
    visited = [False for _ in range(n+1)]
    for u, v, w in paths:
        adj[u].append((w, v))
        adj[v].append((w, u))

    # 게이트에서 출발하여 경로 찾기
    route = []
    for start in gates:
        q = []
        for inten, nextt in adj[start]:
            heapq.heappush(q, (inten, nextt))
        find_summit()
        # 방문체크 풀기
        while route:
            visited[route.pop()] = False

    return [summit, minIntensity]

if __name__ == '__main__':
    print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
    print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
    print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
    print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
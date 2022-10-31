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
            # if summits_dic[now]:
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

    # 이건 그냥 해봄 안해도 되려나?
    # summits = set(summits)
    summits_dic = {i: False for i in range(1, n+1)}
    for u in summits:
        summits_dic[u] = True

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

# set 사용                                     dic 사용
# 테스트 1 〉	통과 (0.03ms, 10.3MB)           테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.1MB)           테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)           테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)           테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.05ms, 10.2MB)           테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.10ms, 10.2MB)           테스트 6 〉	통과 (0.10ms, 10.4MB)
# 테스트 7 〉	통과 (0.10ms, 10.4MB)           테스트 7 〉	통과 (0.10ms, 10.3MB)
# 테스트 8 〉	통과 (0.09ms, 10.3MB)           테스트 8 〉	통과 (0.06ms, 10.3MB)
# 테스트 9 〉	통과 (0.13ms, 10.2MB)           테스트 9 〉	통과 (0.09ms, 10.3MB)
# 테스트 10 〉	통과 (0.27ms, 10.2MB)           테스트 10 〉통과 (0.19ms, 10.3MB)
# 테스트 11 〉	통과 (0.38ms, 10.2MB)           테스트 11 〉통과 (0.27ms, 10.2MB)
# 테스트 12 〉	통과 (0.21ms, 10.3MB)           테스트 12 〉통과 (0.33ms, 10.4MB)
# 테스트 13 〉	통과 (5.54ms, 11.8MB)           테스트 13 〉통과 (3.87ms, 11.7MB)
# 테스트 14 〉	통과 (61.44ms, 19.8MB)          테스트 14 〉통과 (60.43ms, 20MB)
# 테스트 15 〉	통과 (601.54ms, 74.5MB)         테스트 15 〉통과 (541.17ms, 74.7MB)
# 테스트 16 〉	통과 (392.12ms, 77.1MB)         테스트 16 〉통과 (400.99ms, 77.3MB)
# 테스트 17 〉	통과 (403.62ms, 77.1MB)         테스트 17 〉통과 (320.63ms, 77.4MB)
# 테스트 18 〉	통과 (64.40ms, 16.4MB)          테스트 18 〉통과 (30.89ms, 16.6MB)
# 테스트 19 〉	통과 (117.37ms, 36.6MB)         테스트 19 〉통과 (104.40ms, 36.6MB)
# 테스트 20 〉	통과 (513.29ms, 89.9MB)         테스트 20 〉통과 (422.74ms, 93.7MB)
# 테스트 21 〉	통과 (712.31ms, 78.6MB)         테스트 21 〉통과 (590.71ms, 83MB)
# 테스트 22 〉	통과 (28.41ms, 15.6MB)          테스트 22 〉통과 (32.94ms, 16MB)
# 테스트 23 〉	통과 (125.92ms, 34.5MB)         테스트 23 〉통과 (70.84ms, 35.4MB)
# 테스트 24 〉	통과 (121.16ms, 30.9MB)         테스트 24 〉통과 (75.07ms, 31.7MB)
# 테스트 25 〉	통과 (431.88ms, 93.3MB)         테스트 25 〉통과 (290.28ms, 96.7MB)

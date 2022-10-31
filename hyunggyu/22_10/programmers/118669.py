import heapq
def solution(n, paths, gates, summits):
    min_summits = min(summits)
    graph = {}
    for _ in range(1,n+1):
        graph[_] = []
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    def solve(n,tmp):
        q = []
        for now in gates:
            for next, nxt_cnt in graph[now]:
                heapq.heappush(q,(nxt_cnt,next,0,now))
        while q:
            cnt, now,l,past = heapq.heappop(q)
            if cnt > tmp:
                return
            if l > n:
                continue
            if now in gates:
                continue
            if now in summits:
                heapq.heappush(result,(now,cnt))
                tmp = cnt
                if now == min_summits:
                    return
                continue
            for next, nxt_cnt in graph[now]:
                if next == past or nxt_cnt > tmp:
                    continue
                if nxt_cnt > cnt:
                    heapq.heappush(q,(nxt_cnt,next,l+1,now))
                else:
                    heapq.heappush(q,(cnt,next,l+1,now))

    # 한번에 mt를 다 넣어서 거기에 해당하는 도착장소 + w를 힙으로 넣어서 계산!
    # 하나라도 나오면 바로 결과 도출? 대신 힙으로 할때 2번째 인자도 비교사항에 들어가야한다!
    result = []
    solve(n,int(1e7))
    answer = list(heapq.heappop(result))
    return answer
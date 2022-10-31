# 질문하기 참고 코드
import heapq


def solution(n, paths, gates, summits):
    weights = [[] for _ in range(n + 1)]  # 변경점1: weights 구조 다름
    for i, j, w in paths:
        weights[i].append((j, w))
        weights[j].append((i, w))
    INF = 10_000_000
    min_intensities = [INF] * (n + 1)
    hq = []
    summits = set(summits)  # 변경점2: set에서의 in 연산자는 시간 복잡도가 O(1)
    
    for gate in gates:
        heapq.heappush(hq, (0, gate))
        min_intensities[gate] = 0
    
    while hq:
        intensity, v = heapq.heappop(hq)
        if v in summits or intensity > min_intensities[v]:
            continue
        for nv, next_intensity in weights[v]:
            next_intensity = max(intensity, next_intensity)
            if next_intensity < min_intensities[nv]:
                min_intensities[nv] = next_intensity
                heapq.heappush(hq, (next_intensity, nv))
        
    answer_cand = [[summit, min_intensities[summit]] for summit in summits]
    answer_cand.sort(key=lambda x: (x[1], x[0]))
    answer = answer_cand[0]
    
    return answer


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))

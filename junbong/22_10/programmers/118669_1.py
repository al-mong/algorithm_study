'''
테스트 1 〉	    통과 (0.02ms, 10.3MB)
테스트 2 〉	    통과 (0.02ms, 10.2MB)
테스트 3 〉 	통과 (0.02ms, 10.2MB)
테스트 4 〉	    통과 (0.01ms, 10.2MB)
테스트 5 〉 	통과 (0.03ms, 10.1MB)
테스트 6 〉	    통과 (0.17ms, 10.3MB)
테스트 7 〉	    통과 (0.19ms, 10.3MB)
테스트 8 〉	    통과 (0.31ms, 10.2MB)
테스트 9 〉	    통과 (0.66ms, 10.2MB)
테스트 10 〉	통과 (1.91ms, 10.4MB)
테스트 11 〉	통과 (1.66ms, 10.3MB)
테스트 12 〉	통과 (4.31ms, 10.4MB)
테스트 13 〉	통과 (53.46ms, 12.7MB)
테스트 14 〉	통과 (166.22ms, 23.4MB)
테스트 15 〉	통과 (298.68ms, 53.6MB)
테스트 16 〉	통과 (1049.62ms, 118MB)
테스트 17 〉	통과 (1195.47ms, 118MB)
테스트 18 〉	통과 (83.69ms, 12.8MB)
테스트 19 〉	통과 (330.51ms, 23.7MB)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	실패 (시간 초과)
테스트 22 〉	통과 (5688.55ms, 777MB)
테스트 23 〉	실패 (시간 초과)
테스트 24 〉	실패 (시간 초과)
테스트 25 〉	실패 (시간 초과)

-- 시간초과 원인 --
weights 구조 차이
summits를 리스트로 놔두고 품 => in 연산자 속도 차이
'''
<<<<<<< HEAD
=======

>>>>>>> ab90105ed3fa60fcd4ee23bf54f9c3cd56429c8f
import heapq


def solution(n, paths, gates, summits):
    weights = [[0] * (n + 1) for _ in range(n + 1)]  # 가중치 배열
    for i, j, w in paths:
        weights[i][j] = w
        weights[j][i] = w
    INF = 10_000_000
    min_intensities = [INF] * (n + 1)  # 해당 노드까지의 intensity 저장할 리스트
    hq = []  # 힙큐 리스트
    
    for gate in gates:
        heapq.heappush(hq, (0, gate))  # 출입구 전부 힙큐에 넣어놓기
        min_intensities[gate] = 0  # 출입구의 intensity는 0
    
    while hq:
<<<<<<< HEAD
        v, intensity = heapq.heappop(hq)
=======
        intensity, v = heapq.heappop(hq)
>>>>>>> ab90105ed3fa60fcd4ee23bf54f9c3cd56429c8f
        # 시작점은 min_intensity가 0 이므로 in으로 확인안해도 됨
        if v not in summits and intensity <= min_intensities[v]:  
            for nv in range(1, n + 1):
                if weights[v][nv]:  # 길이 있으면
                    # 현재 노드까지의 intensity와 다음 등산로 시간이랑 비교
                    next_intensity = max(intensity, weights[v][nv])
                    # nv 노드까지 기존보다 더 작은 intensity로 갈수있다면 갱신해줌
                    if next_intensity < min_intensities[nv]:
                        min_intensities[nv] = next_intensity
                        heapq.heappush(hq, (next_intensity, nv))
    
    # summit 중 최소 intensity 찾기
    min_intensity = INF
    for summit in summits:
        min_intensity = min(min_intensities[summit], min_intensity)
    
    min_summit = n
    for summit in summits:
        if min_intensities[summit] == min_intensity:
            min_summit = min(summit, min_summit)

    answer = [min_summit, min_intensity]

    return answer


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))

import itertools

# 모든 순열 완전탐색
def solution(k, dungeons):
    max_count = 0
    for per in itertools.permutations(dungeons, len(dungeons)):     
        count = 0
        kk = k
        for p in per:
            if kk >= p[0]:
                count += 1
                kk -= p[1]
        max_count = max(max_count, count)

    return max_count

if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
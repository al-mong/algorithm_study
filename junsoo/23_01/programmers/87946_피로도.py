from itertools import permutations
def solution(k, dungeons):
    length = len(dungeons)
    dungeon_list = [i for i in range(length)]
    permutation = permutations(dungeon_list, length)    #모든 순열 생산
    # print(list(permutation))

    def check(per, idx, k, result):   # 순열, 순열 인덱스, 남은 피로도, 값 저장소
        if idx == length or k < dungeons[per[idx]][0]:  # 전부 탐색했거나, 남은 피로도가 필요 피로도보다 적으면
            return result
        else:
            k -= dungeons[per[idx]][1]
            return check(per, idx+1, k, result+1)

    answer = -1
    for per in permutation:
        result = check(per, 0, k, 0)
        if answer < result:
            answer = result

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
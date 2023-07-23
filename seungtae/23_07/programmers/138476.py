from collections import defaultdict

def solution(k, tangerine):
    c_dict = defaultdict(int)
    for t in tangerine:
        c_dict[t] += 1
    c_list = list(c_dict.values())
    c_list.sort(reverse=True)

    answer = 0
    select = 0
    while select < k:
        select += c_list[answer]
        answer += 1

    return answer

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))
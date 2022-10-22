def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    danger = dict()  # 신고 당한 사람 : {신고자}
    for i in report:
        a, b = map(str, i.split())
        # a = 신고자, b = 신고당한 사람

        if danger.get(b):
            danger[b].add(a)
        else:
            danger[b] = {a}

    for b, aaa in danger.items():
        if len(aaa) >= k:
            for i in aaa:
                answer[id_list.index(i)] += 1

    return answer
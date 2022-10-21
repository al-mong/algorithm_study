def solution(id_list, report, k):
    report_dic = {id_list[i]:[0, set()] for i in range(len(id_list))}
    answer = [0 for _ in range(len(id_list))]
    
    for r in report:
        f, t = r.split()
        if f not in report_dic[t][1]:
            report_dic[t][0] += 1
            report_dic[t][1].add(f)
            
    for v in report_dic.values():
        if v[0] >= k:
            for name in v[1]:
                answer[id_list.index(name)] += 1
            
    return answer
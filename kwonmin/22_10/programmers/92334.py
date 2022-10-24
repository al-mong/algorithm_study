def solution(id_list, report, k):
    id_dict = {name:[] for name in id_list}
    report = list(set(report))
    for rep in report:
        s, p = rep.split()
        id_dict[p].append(s)
    
    res_dict = {name:0 for name in id_list}
    
    for key, val in id_dict.items():
        if len(val) >= k:
            for id in val:
                res_dict[id] += 1
    

    answer = list(res_dict.values())
    return answer
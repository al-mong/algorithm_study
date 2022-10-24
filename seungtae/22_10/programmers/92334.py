def solution(id_list, report, k):
    
    answer = [0 for _ in range(len(id_list))]
    count = [0 for _ in range(len(id_list))]
    name_index_dic = {}
    report_name_dic = {i: [] for i in range(len(id_list))}
    
    for i in range(len(id_list)):
        name_index_dic[id_list[i]] = i
    
    report = list(set(report))
    
    for info in report:
        x, y = info.split()
        report_name_dic[name_index_dic[y]].append(name_index_dic[x])
        count[name_index_dic[y]] += 1

    for i in range(len(count)):
        if count[i] >= k:
            for people in report_name_dic[i]:
                answer[people] += 1
                
    return answer
def solution(new_id):
    ok_list = ['0','1','2','3','4','5','6','7','8','9','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','-','_','.']
    new_id = new_id.lower()
    id_rst = list(new_id)
    new_id = ''
    for i in range(len(id_rst)):
        if id_rst[i] not in ok_list:
            continue
        if id_rst[i] == '.':
            if new_id:
                if new_id[-1] != '.':
                    new_id = new_id + id_rst[i]
        else:
            new_id = new_id + id_rst[i]
    if not new_id:
        new_id += 'a'
    new_id = new_id.strip('.')
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.strip('.')
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    
    answer = new_id
    return answer


new_id = "abcdefghijklmn.p"
print(solution(new_id))
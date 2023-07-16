# 42842 Ä«Æê

def solution(brown, yellow):
    limit = yellow
    yellowList = []
    tmp = 1
    answer = []
    while tmp <= limit:
        if tmp == limit:
            if tmp <= yellow//tmp:
                yellowList.append((tmp,yellow//tmp))
                limit = yellow//tmp
        elif yellow % tmp == 0:
            yellowList.append((tmp,yellow//tmp))
            limit = yellow//tmp
        tmp += 1
    while yellowList:
        col,row = yellowList.pop()
        if 2*row + 2*col + 4 == brown:
            answer.append(row+2)
            answer.append(col+2)
            break
    return answer
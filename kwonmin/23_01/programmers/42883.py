def solution(number, k):
    stk = []
    for num in number:
        if k > 0:
            if stk:
                if stk[-1] >= num:
                    stk.append(num)
                else:
                    while stk and stk[-1] < num:
                        stk.pop()
                        k -= 1
                        if k == 0:
                            break
                    stk.append(num)
            else:
                stk.append(num)

        else:
            stk.append(num)
    
    while k > 0:
        stk.pop()
        k -= 1
            
    answer = ''.join(stk)
    return answer
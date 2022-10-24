def solution(n, info):
    result = 0
    result_arr = []

    # 어떤 것을 이기는 지
    def search(n,m,k,total):
        nonlocal result
        nonlocal result_arr
        if total < 0:
            return
        if n == m-1:
            if total <= k:
                tmp = k - total
                cnt = 0
                for j in range(10):
                    if count[j] == info[j]:
                        continue
                    elif count[j] > info[j]:
                        cnt += (10-j)
                    else:
                        cnt -= (10-j)
                if cnt < 0:
                    return
                elif cnt > result:
                    result = cnt
                    result_arr = count[:]
                    result_arr[10] = tmp
                elif cnt == result:
                    if tmp > result_arr[10]:
                        ck = 1
                    else:
                        for j in range(9,-1,-1):
                            if result_arr[j] < count[j]:
                                ck = 1
                                break
                            elif result_arr[j] > count[j]:
                                ck = 0
                                break
                    if ck:
                        result_arr = count[:]
                        result_arr[10] = tmp
            return
        count[n] = info[n] + 1
        search(n+1,m,k,total-count[n])
        count[n] = 0
        search(n+1,m,k,total)
    count = [0]*11
    search(0,10,n,n)
    if result == 0:
        answer = [-1]
    else:
        answer = result_arr[:]
    return answer
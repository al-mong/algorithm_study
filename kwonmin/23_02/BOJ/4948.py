while True:
    N = int(input())
    if N == 0:
        break
    end = ((2*N)+1)
    DP = list(range(end))
    res = 0
    for i in range(2, end):
        if DP[i] != 0:
            if i > N:
                res += 1
            cnt=i
            while cnt < end:
                if DP[cnt] != 0:
                    DP[cnt] = 0
                cnt += i

    print(res)
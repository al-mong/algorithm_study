n = int(input())

left = tuple(map(int, input().split()))

result = [n for _ in range(n)]

def line(result, k=1):
    global n
    # print(*result)
    if k == n and sum(result) == n*(n+1)//2:
        print(*result)
        return

    for i in range(n):
        if result[i] != n:
            continue

        result[i] = k

        ck = 0
        for j in result[:result.index(k)]:
            if j > k:
                ck += 1

        if ck != left[k-1]:
            result[i] = n
            continue

        line(result[:], k+1)

line(result)
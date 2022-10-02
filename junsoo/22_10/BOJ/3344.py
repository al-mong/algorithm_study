def dfs():
    global result

    deep = len(chess)   # 이번에 넣을 인덱스
    if len(chess) != n:
        for q in range(n):
            if not used[q]:

                escape = 0
                for i, v in enumerate(chess):
                    a = q - (deep - i)
                    b = q + (deep - i)
                    if 0 <= a:
                        if a == chess[i]:
                            escape = 1
                            break
                    if b < n:
                        if b == chess[i]:
                            escape = 1
                            break
                if escape:
                    continue

                chess.append(q)
                used[q] = 1
                dfs()
                chess.pop()
                used[q] = 0

    else:
        result += 1

n = int(input())
result = 0
chess = []
used = [0 for _ in range(n)]
dfs()

print(result)
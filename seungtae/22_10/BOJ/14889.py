import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r = n // 2

# 조합 구하기
def nCr(n, r, s):
    global count, minV
    if count == ncr // 2:       # 조합 반 구하면 종료
        return
    if r == 0:
        count += 1              # 조합 하나 구할 때마다 카운트 + 1
        r_comb = list(set(A) - set(comb))       # 한팀이 정해지면 다른팀도 차집합으로 구하기

        comb_total = 0                          # 스타트 팀 점수 계산 ~~
        for i in range(len(comb)):
            for j in range(len(comb)):
                if i == j:
                    continue
                comb_total += arr[comb[i]][comb[j]]

        r_comb_total = 0                        # 링크 팀 점수 계산 ~~
        for i in range(len(r_comb)):
            for j in range(len(r_comb)):
                if i == j:
                    continue
                r_comb_total += arr[r_comb[i]][r_comb[j]]

        minV = min(minV, abs(comb_total - r_comb_total))    # 점수 차이 갱신
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)


# nCr 구하기
def factorial(k):
    fact = 1
    for i in range(1, k+1):
        fact *= i
    return fact

def nCr_cal(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

ncr = int(nCr_cal(n, r))

A = list(range(n))
comb = [0] * r

minV = sys.maxsize

count = 0
nCr(n, r, 0)
print(minV)

'''
사자를 최대 n마리까지 배치 가능
사자      가능
0           1
1           2n
2           n*(n-1)/2 - 2*(n-1)
3           nC3 -
'''

def lion(n):
    if n == 1:
        result[n] = 3
    elif n == 2:
        result[n] = 7
    else:
        result[n] = result[n - 1]
        ck = 1
        while n - ck != 1:
            ck += 1
            result[n] += 2*result[n-ck]
                    #  없을 때     좌우측 있을 때

n = int(input())

result = [0 for i in range(n + 1)]
for i in range(1, n+1):
    lion(i)
print(result[n])


'''
실버1. 일단 아무거도 없는 경우도 생각해야해서 0 인덱스에
1 놔둠. 그리고 이제 사자가 없는 경우와 있는 경우를 나눠서 생각하면 됨
노가다로 2 인덱스까지 dp 값 채워두고, dp 에 0 채워두고
규칙성을 찾아내보니 사자가 없는 경우에는 없는거, 왼쪽있는거, 오른쪽있는거
3가지 경우의 수가 나옴. 있는 경우는 없는거, 왼쪽 or 없는거, 오른쪽 2가지 경우가 나옴
그래서 다음의 주석의 식이 나오고 풀어서 for 문에 적으면 됨.
# dp[i-2] * 3 + (dp[i-1]-dp[i-2]) * 2

N = int(input())
dp = [1, 3, 7] + [0] * (N-2)
for i in range(3, N+1):
    dp[i] = (dp[i-2] + dp[i-1] * 2) % 9901
print(dp[N])
'''
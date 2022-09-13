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
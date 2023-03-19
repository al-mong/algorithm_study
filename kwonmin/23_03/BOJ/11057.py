from sys import stdin; input = stdin.readline

# 1일땐 10
# 2일 땐 10+9+8+7+6+5+4+3+2+1
# 3일 땐 10+(10+9+8+7+6+5+4+3+2+1)+9(9+8+7+6+5+4+3+2+1)+...
# 왼쪽이랑 위랑 값 가져오면 됨
# 왼쪽에서 이미 계산된 값들이기 때문

N = int(input())

if N == 1:
    print(10)
    exit()

field = [[1]+[0]*9 for _ in range(N)]
for i in range(1,10):
    field[0][i] = 1

for i in range(1,N):
    for j in range(1,10):
        field[i][j] = field[i-1][j] + field[i][j-1]

print(sum(field[N-1])%10007)

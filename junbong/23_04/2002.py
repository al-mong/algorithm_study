# 230416
import sys
input = sys.stdin.readline

N = int(input())
t_in = {input().rstrip(): i for i in range(N)}
t_out = [0] * N

cnt = 0
for _ in range(N):
    in_number = t_in[input().rstrip()]
    before_sum = sum(t_out[:in_number])
    if before_sum < in_number:
        cnt += 1
    t_out[in_number] = 1

print(cnt)

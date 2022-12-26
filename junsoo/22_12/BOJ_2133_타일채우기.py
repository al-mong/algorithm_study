# 홀수는 불가능
result = [0 for _ in range(31)]
result[2] = 3
# result[4] = result[2] * result[2] + 2
# result[6] = result[2] * result[4] + 2 * result[2] + 2
# result[8] = result[2] * result[6] + 2 * result[4] + 2 * result[2] + 2
for i in range(4, 31, 2):
    result[i] = result[i-2] * 3 + sum(result[:i-2:2]) * 2 + 2
print(result[int(input())])
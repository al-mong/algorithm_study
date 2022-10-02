n = int(input())
stat = []
for _ in range(n):
    stat.append(list(map(int, input().split())))

print(list(zip(stat, zip(*stat))))
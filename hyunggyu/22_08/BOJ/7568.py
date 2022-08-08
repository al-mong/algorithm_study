T = int(input())
b = []
for i in range(T):
    a = list(map(int,input().split()))
    b.append(a)
c = [1]*T # [0,0,0,0,0]
for i in range(T):# 55 58 88 60 46
    for j in range(T): # 185 183 186 175 155
        if b[i][0] < b[j][0] and b[i][1] < b[j][1]:
            c[i] += 1
for i in range(len(c)):
    print(c[i], end=" ")
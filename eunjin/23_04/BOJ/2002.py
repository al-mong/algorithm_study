n=int(input())
li = []
lili = []
ans = 0

for i in range(n):
    li.append(input())

for j in range(n):
    lili.append(input())

for k in range(n-1):
    for l in range(k+1,n):
        if li.index(lili[k]) > li.index(lili[l]):
            ans += 1
            break

print(ans)

a = list(map(int,input().split()))
if a[1] <45:
    a[1] = a[1] + 15
    if a[0] == 0:
        a[0] = 23
    else:
        a[0] -= 1
else:
    a[1] = a[1] -45
print(a[0],a[1])


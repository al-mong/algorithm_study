num = int(input())
if num < 100:
    print(num)
elif num == 1000:
    print(144)
else:
    
    count = 99
    for j in range(100,num+1):
        a = []
        for i in str(j):
            a.append(int(i))
        if a[0]-a[1] == a[1]-a[2]:
            count +=1
    print(count)


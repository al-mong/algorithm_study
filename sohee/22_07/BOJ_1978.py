a = int(input())
num1 = list(map(int, input().split()))



b = []
for i in range(a):
    if num1[i] == 1:
        continue
    elif num1[i] == 2:
        b.append(2)
    else:
        num2 = list(range(2, num1[i]))
        count = 0
        for c in num2:
            if num1[i] % c == 0:
                count += 1
        if count == 0:
            b.append(num1[i])
print(len(b))           
            

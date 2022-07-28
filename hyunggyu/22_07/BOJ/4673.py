def self_num(d):
    d = str(d)
    result = 0
    for i in d:
        result += int(i)
    result += int(d)
    return result

sult = list(range(1,10001))
for i in range(1,10001):
    a = self_num(i)
    if  a in sult:
        sult.pop(sult.index(a))
for i in sult:
    print(i)

# 9999 = 9999-36 = 9963
# 101 = 100-2 

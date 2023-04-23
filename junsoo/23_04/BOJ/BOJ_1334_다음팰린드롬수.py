n = input()
rev_n = n[::-1]
length = len(n)

result = n[:length//2] + rev_n[length//2:]
if int(result) > int(n):
    print(result)
else:   # 가운데 숫자 + 1
    n = str(int(n) + 10**(length//2))
    rev_n = n[::-1]
    length = len(n)
    result = n[:length // 2] + rev_n[length // 2:]
    print(result)
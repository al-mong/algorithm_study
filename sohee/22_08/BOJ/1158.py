# 실버4. 요세푸스문제.

# 이렇게 풀었는데, 이중 for문이라 그런지 시간초과됨..
# a, b = list(map(int, input().split()))
# c = list(range(1, a+1))
# d = []
# for i in range(a): # 입력한 숫자만큼 for문 돌아야함. 각각 제거하고 d에 추가해야해서.
#     for k in range(1, b):
#         c.append(c.pop(0))
#     d.append(c.pop(0))
# print("<", ', '.join(str(i) for i in d), ">", sep = '')



# 구글링 해옴... 혼자힘으로 도저히 못풀겠음...
n, k = list(map(int, input().split()))
c = list(range(1, n+1))
ans = []
num = k - 1

for i in range(1, n+1):
    if len(c) > num:
        ans.append(c.pop(num))
        num += k - 1
    elif len(c) <= num:
        num = num % len(c)
        ans.append(c.pop(num))
        num += k - 1
print("<", ', '.join(str(i) for i in ans), ">", sep = '')
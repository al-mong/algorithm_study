# 수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

# N == 1, 10
# N == 2, 55
# N == 3, 220
# N == 4, 715  
# N == 5, 2002  >> 확인 필요 ok

# 0-9 = 55      220     715
# 1-9 = 45      165     495
# 2-9 = 36      120     330
# 3-9 = 28      84      210
# 4-9 = 21      56      126
# 5-9 = 15      35      70
# 6-9 = 10      20      35
# 7-9 = 6       10      15
# 8-9 = 3       4       5
# 9-9 = 1       1       1


N = int(input()) -1
nums = [i for i in range(1, 11)]

while N:
    N -= 1
    new_nums = []
    tmp = 0
    for i in nums:
        tmp += i
        new_nums.append(tmp)
    nums = new_nums

print(nums[-1] % 10007)

# a, b, c, d, e = 0, 0, 0, 0, 0
# result = 1
# while True:
#     e += 1
#     if e == 10:
#         e = 0
#         d += 1
#         if d == 10:
#             c += 1
#             d = 0
#             if c == 10:
#                 b += 1
#                 c = 0
#                 if b == 10:
#                     a += 1
#                     b = 0
#                     if a == 10:
#                         break
    
#     if a <= b and b <= c and c <= d and d<=e:
#         result += 1
#         # print(a, b, c,d)
# print(result)


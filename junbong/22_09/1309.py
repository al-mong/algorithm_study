# 220911

'''
# N = 1 일 때 ===============================================

x | x   o | x   x | o

=> 경우의 수: 3


# N = 2 일 때 ===============================================

x | x   x | x   x | x
x | x   o | x   x | o

=> N - 1 우리에서 마지막 줄에 사자가 없는 경우
N번 줄에서 사자 배치의 경우의 수는 [없, 왼, 오]

o | x   o | x
x | x   x | o

=> N - 1 우리에서 마지막 줄에 사자가 왼쪽에 있는 경우
N 줄에서 나올 수 있는 경우의 수는 [없, 오]

x | o   x | o
x | x   o | x

=> N - 1 우리에서 마지막 줄에 사자가 오른쪽에 있는 경우
N 줄에서 나올 수 있는 경우의 수는 [없, 왼]


# 결론 ================================================
N번 줄에 사자가 없는 경우는 아무데나 나올 수 있다
왼쪽에 있는 경우는 N - 1번 줄에 사자가 없거나, 오른쪽에 있거나
오른쪽에 있는 경우는 N - 1번 줄에 사자가 없거나, 왼쪽에 있거나
'''

# N = 0일 때 (있다고 가정)
no, left, right = 1, 0, 0

for i in range(int(input())):
    former_no = no
    former_left = left
    former_right = right
    no = former_no + former_left + former_right
    left = former_no + former_right
    right = former_no + former_left

print((no + left + right) % 9901)


import sys
input = sys.stdin.readline

def sorting(A, B):
    rst = []
    while A and B:
        # pop을 쓸까?
        a = A[0]
        b = B[0]
        if a < b :
            rst.append(A.pop(0))
        else:
            rst.append(B.pop(0))
    rst.extend(A)
    rst.extend(B)
    return rst


N = int(input())
nums = [[float(input()) for _ in range(N)]]
# 생각부터 적자
# 파이썬은 슬라이싱을 쓰면 될 듯
# pop과 append를 쓰는 건 어떨까
# 이중 리스트로 만들어 둠
# 원소 하나 꺼냄(팝) - 반으로 슬라이싱해서 나눠담음 - 리스트에 어펜드

while len(nums) < N:
    num = nums.pop(0)
    if len(num) % 2:
        num_a, num_b = num[0:len(num)//2+1], num[len(num)//2+1:]
    else:
        num_a, num_b = num[0:len(num)//2], num[len(num)//2:]
    if len(num_a)>0:        
        nums.append(num_a)
    if len(num_b)>0:
        nums.append(num_b)
# 이러면 각각의 요소들이 리스트 형태로 나뉘어서 들어간다.
# 길이 절반만큼 반복하면서, len이 1이 될 때까지 반복

while len(nums)>1:
    o = nums.pop(0)
    p = nums.pop(0)
    nums.append(sorting(o,p))

for n in range(7):
    print(f'{nums[0][n]:.3f}')

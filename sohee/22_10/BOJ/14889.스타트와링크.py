import sys
input = sys.stdin.readline

# 순열구하기. 1이 포함된 경우와 포함되지 않는 경우로 나눌거임.
def nCr(n, r, s):
    if r == 0:
        if 1 in comb[:]:  # 1이 포함되면 comb_list1에 추가하기
            comb_list1.append(comb[:])
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

N = int(input())
A = list(range(1,N+1))
n = len(A)
r = N // 2
comb = [0] * r
arr = [list(map(int, input().split())) for i in range(N)]
comb_list1 = []  # 1이 포함된 집합을 포함할 리스트
nCr(n, r, 0)

comb_list2 = []  # comb_list1과 대칭인 리스트. set을 통해서 나머지구하기
for i in range(len(comb_list1)):
    comb_list2.append(list(set(A) - set(comb_list1[i])))

# 한팀당 쓰는 칸수가 r(r-1)
cha_min = 1000000  # 임의의 최대값 적어놓기, 근데 여기서 N 최대가 2이고, 값 최대가 100이라 최대차이는 9000임!!
i = 0
while i < len(comb_list1):
    total1 = 0
    total2 = 0
    for s in comb_list1[i]:  # 팀1의 값 구하기
        for h in comb_list1[i]:
            if s != h:
                total1 += arr[s-1][h-1]

    for s in comb_list2[i]:  # 팀2의 값 구하기
        for h in comb_list2[i]:
            if s != h:
                total2 += arr[s-1][h-1]

    if abs(total1 - total2) < cha_min:  # 차이의 최소값 구하기
        cha_min = abs(total1 - total2)
    i += 1
print(cha_min)
                


from itertools import combinations


N = int(input()) # 짝수개 들어옴
field = [list(map(int,input().split())) for _ in range(N)] # 시너지 값 입력하기
# N//2 개 선택하는 알고리즘을 짜면 됨
nums = set(range(N)) # 인덱스값 모음. 여기서 절반씩 A랑 B가 나눠가짐
# As = list(map(list,combinations(nums, N//2))) # A가 N//2씩 가질 수 있는 모든 경우의 수. 기본으로 튜플로 받아오는데 리스트로 받고 싶으면 이렇게.
# 생각해보니까 이거 백트래킹 할거면 절반만 하면 되지 않나...? 흠
As = combinations(nums, N//2)
mins = 4000000 # 최소값 미리 설정
for A in As: # 경우의 수 하나씩 뽑아오기
    B = list(nums-set(A)) # B의 원소는 nums에서 A에 속하지 않은 아이들
    asum = 0
    bsum = 0
    for i in range(N): 
        for j in range(N): # 이중 포문을 돌면서 A와 B에 시너지값 채우기
            if i in A and j in A:
                asum += field[i][j]
            if i in B and j in B:
                bsum += field[i][j]

    if abs(asum-bsum) < mins: # 시너지값의 차이와 최소값 비교하기
        mins = abs(asum-bsum) # 최소값이라면 교체
print(mins)
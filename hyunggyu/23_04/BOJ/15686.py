# n*n 도시
# r 행 c열
# 도시의 치킨 거리는 모든 치킨 거리의 합
# # 1 집 2 치킨집
# 치킨집 최대 개수 m개로 나머지 폐업
n,m = map(int, input().split())
INF = int(1e9) # 최댓값(치킨거리의)
arr = [list(map(int, input().split())) for _ in range(n)]
house = []
# 집 위치를 넣자
c_house= []
for j in range(n):
    for i in range(n):
        if arr[j][i] == 1:
            house.append((i,j))
        elif arr[j][i] == 2:
            c_house.append((i,j))
a = len(house)
# 집의 개수 a
b = len(c_house)
# 치킨집의 개수 b

def howlong(idx_a, idx_b):
    d = abs(house[idx_a][0] - c_house[idx_b][0]) + abs(house[idx_a][1] - c_house[idx_b][1])
    return d
 
arr = list(range(b)) # b 개 중에서 m개 조합으로구현
chosen = [-1]*m
comb_result = []
def comb(n,m,j):
    if n == m:
        comb_result.append(chosen[:])
        return
    for i in range(j,len(arr)):
        chosen[n] = arr[i]
        comb(n+1,m,i+1)
comb(0,m,0)
result = [INF]*a
for idx in range(len(comb_result)): #  i = [1,2..m개]
    # 경우의 수에 따른 인덱스를 넣어서 치킨 거리를 모두 구한 다음 최소값에 이를 때 거리를 출력
    tmp = [INF]*a
    for j in range(a):
        # 모든 집에 대해서
        cnt = INF
        for i in comb_result[idx]:
            # 정해진 치킨 집중 가장 가까운 곳을 찾으면
            d = howlong(j,i)
            if d < cnt:
                cnt = d
        tmp[j] = cnt
    if sum(result) > sum(tmp):
        result = tmp[:]
print(sum(result))
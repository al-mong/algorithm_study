# 현재 피로도, 던전리스트[최소필요피로도,소모피로도]
k= 80
dungeons = [[80, 20], [50, 40], [30, 10]]

# 돌수 있는 던전 개수
answer = 0

data = [[] for _ in range(1001)]
for i in range(len(dungeons)):
    data[dungeons[i][1]].append(dungeons[i][0])
for i in range(1001):
    data[i].sort(reverse=True)
for i in range(1001):
    for j in range(len(data[i])):
        if data[i][j] < k:
            print(data[i][j])
            answer += 1
            k -= i
    


print(answer)
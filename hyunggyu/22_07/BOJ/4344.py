T = int(input())
avg = 0
result = 0
for t in range(T):
    count = 0
    score = list(map(int,input().split()))
    avg = sum(score[1:])/score[0]
    for i in score[1:]:
        if i > avg:
            count +=1
    result = round(count*100/score[0],3)
    print('{:.3f}%'.format(result))
# 입력
    5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
score = []
for _ in range(int(input())):
    score.append(float(input()))
score = [score]

print("나누기")
print(score)
while len(score[-1]) != 1:                  # 왼, 오 리스트로 반 나눌때 항이 홀수개면 오른쪽이 더 크기가 큼
    for i in range(len(score)):             # 오른쪽 리스트 크기가 1이 될때까지 계속 반으로 나눔!
        mid = len(score[0]) // 2
        score.append(score[0][:mid])
        score.append(score[0][mid:])
        score.pop(0)
    print(score)

print()
print("합치기")
print(score)
result = []
while len(score) != 1:
    for _ in range(len(score) // 2):
        temp = []
        while score[0] or score[1]:             # left 리스트, right 리스트 둘 다 pop 다될때까지 무한루프!!
            if not score[0]:                        # left 리스트 비어있으면 오른쪽에서 팝
                temp.append(score[1].pop(0))                            
            elif not score[1]:                      # right 리스트 비어있으면 왼쪽에서 팝
                temp.append(score[0].pop(0))            
            else:                                   # 둘 다 안비어 있으면 왼, 오 중에 작은거 팝
                if score[0][0] > score[1][0]:         
                    temp.append(score[1].pop(0))
                else:
                    temp.append(score[0].pop(0))
        score.append(temp)
        score.pop(0)
        score.pop(0)
    print(score)

for i in range(7):
    print(f'{score[0][i]:0.3f}')
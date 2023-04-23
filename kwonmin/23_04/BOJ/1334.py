# 왜 많은 조건 분기일까. 흠...
# 시간초과의 느낌이 좀 난다

# 리스트로 받는 방법을 생각
# 첫번째와 1의 자리를 비교한다.
# 첫번째보다 1의 자리가 더 작을 경우 : 자릿수 맞추기.
# 아 자릿수 벗어나는 경우가 없을듯? 흠

start = list(map(int, str(int(input()) + 1)))

if len(start) == 1:
    print(start[0])
    exit()

for _ in range(len(start)):
    for i in range(0, len(start)//2):
        stt = i
        end = -(i+1)
        
        if start[stt] > start[end]:
            start[end] = start[stt]
        elif start[stt] < start[end]:
            start[end] = start[stt]
            start[end-1] += 1

            if start[end-1] > 9:
                for j in range(len(start)-1, 0, -1):
                    if start[j] > 9:
                        start[j] = 0
                        start[j-1] += 1
        


result = "".join(str(s) for s in start)
print(result)


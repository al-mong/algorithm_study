# 좀 귀찮은 문제가 있네
# 원본 그대로 출력해야 한다는 문제...
# 아스키로 하면 어떨까? 라는 생각이 들었지만
# 10만 범위라서 곤란할듯?
# 그럼 숫자만 비교를 해야 하는데


def divide(x):
    head = ''
    number = ''
    tail = ''

    start = 0
    end = len(x)
    flag = True
    for i in range(len(x)):
        if x[i].isnumeric():
            if not start:
                flag = False
                start = i
        
        elif not flag:
            end = i
            break
    
    head = x[:start]
    number = x[start:end]
    tail = x[end:]
    return (head, number, tail)

def solution(files):
    answer = []
    temp = []
    for file in files:
        temp.append(divide(file))

    temp.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for a,b,c in temp:
        answer.append(a+b+c)
    return answer

print(solution(["img12", "img10", "img02", "img1", "IMG01.GIF", "img2.JPG"]))

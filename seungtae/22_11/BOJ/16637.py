# 괄호를 추가하는 경우의 수를 모두 구해서 브루트포스를 구현하는 문제
# 1. 연산자 개수의 길이만큼 배열을 만들어 괄호를 추가할건지 안할건지 1/0 으로 표시한다
# 2. 첫번째 연산자에는 괄호를 추가할 필요가 없다.
# 3. 어떤 연산자에 괄호를 추가하기로 했으면 앞뒤의 연산자에는 괄호를 추가할 수 없다

# 그 후는 연산을 통해 계산하여 맥스값을 추출


from collections import deque

def f(i):
    global sik
    if i == n//2:
        temp1 = deque(sik[:])

        for j in range(n//2):
            if bracket[j]:
                x = int(temp1[2*j])
                y = int(temp1[2*j+2])
                if temp1[2*j+1] == '+':
                    temp1[2*j+2] = str(x + y)
                elif temp1[2*j+1] == '-':
                    temp1[2*j+2] = str(x - y)
                elif temp1[2*j+1] == '*':
                    temp1[2*j+2] = str(x * y)
                temp1[2*j] = 'x'
                temp1[2*j+1] = 'x'

        result = int(temp1[0])
        while temp1:
            giho = temp1.popleft()
            if giho == '+':
                while True:
                    num = temp1.popleft()
                    if num.isdecimal() or len(num) == 2:
                        break
                result += int(num)
            if giho == '-':
                while True:
                    num = temp1.popleft()
                    if num.isdecimal() or len(num) == 2:
                        break
                result -= int(num)
            if giho == '*':
                while True:
                    num = temp1.popleft()
                    if num.isdecimal() or len(num) == 2:
                        break
                result *= int(num)
        ans.append(result)
        return
    else:
        if bracket[i-1]:
            f(i+1)
        else:
            bracket[i] = 1
            f(i+1)
            bracket[i] = 0
            f(i+1)

n = int(input())
sik = list(input())

bracket = [0 for _ in range(n//2)]
ans = []

if n == 1:
    print(int(sik[0]))
else:
    f(1)
    print(max(ans))
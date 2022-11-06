'''
eval(문자열 수식) = 계산해줌, 사칙연산 적용
'''
def answer(new):   # 문자열 수식 계산하기, 한자리 숫자
    ans = ''
    idx = 0
    while idx < len(new):
        if new[idx] == '(':
            tmp = str(eval(new[idx+1] + new[idx+2] + new[idx+3]))
            ans += tmp
            ans = str(eval(ans))
            idx += 5
        elif new[idx] in {'+', '-', '*'}:
            ans += new[idx]
            idx += 1
        else:
            ans = str(eval(ans + new[idx]))
            idx += 1
    ans = int(ans)
    return ans


def check(new, s=0):    # 수식(str), 기호 시작점
    global result

    if s == n//2:
        new += num[-1]
        ans = answer(new)
        if ans > result:
            result = ans
        return
    elif s > n//2:
        ans = answer(new)
        if ans > result:
            result = ans
        return

    tmp = new
    # 안뽑는다
    tmp += num[s] + cal[s]
    check(tmp, s+1)
    # 뽑는다
    new += '(' + num[s] + cal[s] + num[s+1] + ')'
    if s + 1 < n//2:
        new += cal[s+1]
    check(new, s+2)

n = int(input())
word = input()

num = []
cal = []
for i in range(n):
    if i % 2:
        cal.append(word[i])
    else:
        num.append(word[i])

word_new = ''
if n != 1:
    result = float('-inf')
else:
    result = int(word)
check(word_new)
print(result)
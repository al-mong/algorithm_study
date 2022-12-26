# n개 단어, 대문자만 사용
# 알파벳 대문자를 0~9 숫자중 하나로 바꿔 n개 수 합구하기
n = int(input())
arr = list(list(input()) for _ in range(n))

# arr = [['A', 'A', 'A'], ['A', 'A', 'A']]

# 숫자를 읽어야 하고 -> 읽은 것을 임의의 수로 바꿔가면서 덧셈을 해야한다.
# 브루트포스로 풀기 위해서는 N!를 대입해야 한다.

# 모든 숫자의 종류를 가져온다!
value = []
for i in range(n):
    for j in range(len(arr[i])):

        # value에 넣어준다.
        if arr[i][j] in value:
            continue
        else:
            value.append(arr[i][j])

# value = ['A']

# 숫자는 value의 숫자 만큼 9부터 아래로 내려가며 배정한다.
nums = []
for i in range(len(value)):
    nums.append(9-i)

# nums = [9]

# 길이가 가장 긴것의 제일 처음에 가장 큰 숫자를 넣는다!
# 길이가 똑같은 것이 있다면 더 앞에 있는 숫자일수록 큰 점수를 부여한다.
score = {}
for i in value:
    score[i] = [0,i]

for i in range(n):
    L = len(arr[i])
    for j in range(len(arr[i])):
        score[arr[i][j]][0] += 10**L
        L -= 1

# [2220, 'A']

result = list(score[i] for i in value)
result.sort(reverse=True)

appear = {}
for i in range(len(nums)):
    appear[result[i][1]] = nums[i]

# 숫자를 이제 대입하기
answer = 0
for i in range(n):
    tmp = ''
    for j in range(len(arr[i])):
        tmp += str(appear[arr[i][j]])
    answer += int(tmp)
print(answer)
    


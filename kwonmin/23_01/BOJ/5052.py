# 길이순 정렬
# 이게왜트리지? 진짜모름
# 뒤에서부터 비교해야하나?(진짜모름)
# 근데 하나하나 비교하면 시간초과일듯(비교방법 많은데 까먹음)


from sys import stdin; input=stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    nums = [input().strip() for _ in range(N)]
    nums.sort(reverse=True)
    flag = 0
    for i in range(N):
        for j in range(i+1,N):
            if len(nums[i]) > len(nums[j]):
                if nums[i].startswith(nums[j]):
                    flag = 1
                    break
        if flag == 1:
            break
    [print('YES') if not flag else print('NO')]

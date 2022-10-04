"""
가장 빨리 끝낼 수 있는 사람부터 먼저 끝내기
1. sort를 이용하여 작은 값부터 정렬
2. 각 사람들이 기다려야할 시간과
3. 그 시간들의 합을 구하기
"""


N = int(input())
case = list(map(int, input().split()))
case.sort()             # 1. sort를 이용하여 작은 값부터 정렬

my_sum = 0              # 2. 각 사람들이 기다려야할 시간과
time_sum = 0            # 3. 그 시간들의 합을 구하기
for i in case:
    my_sum += i
    time_sum += my_sum

print(time_sum)

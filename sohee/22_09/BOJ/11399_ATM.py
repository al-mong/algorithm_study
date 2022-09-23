'''결국 오름차순으로 정렬해서 반복해서 더하는 문제'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
total = 0
for i in range(N):
    total += arr[i] * (N-i) # 맨앞자리는 N번 더해지고 그 뒤부터는 -1씩 빼서 더해짐
print(total)
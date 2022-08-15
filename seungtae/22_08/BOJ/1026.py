# 시간제한 2초, python 연산 4천만번 가능
# 1 <= N <= 50
# sort 시간 복잡도 O(n log n) => 50 log(2)50 => 282
# max 시간 복잡도 O(n) => 50

# index 함수는 시간 복잡도 없나 ??
# 그래도 일단 시간은 충분할듯

# 풀이
# 설명 : 반복문을 돌며 a 리스트 원소의 최소와 b 리스트 원소의 최대를 곱해서 더하면 합이 최솟값이 된다.
# 1. a 리스트를 sort함.
# 2. b 리스트에서 max값을 추출하여 그 값의 index를 찾고 pop(index) 을 하여 a 리스트 최소값과 곱함과 동시에 b 리스트에서 삭제함 
# 3. 리스트의 길이만큼 2번을 반복문으로 실행, 곱셈 결과를 total에 계속 더함

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()

total = 0
for i in range(n):
    total += a_list[i] * b_list.pop(b_list.index(max(b_list)))
print(total)
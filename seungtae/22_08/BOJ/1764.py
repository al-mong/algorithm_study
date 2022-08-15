# 시간제한 2초, python 연산 4천만번 가능
# N, M <= 500,000
# set(s) & set(t) => O(len(s) * len(t)) => 2500만
# sort() => O(n log n ) => 50만 log(2)50만 => 약 1000만
# 시간이 간당간당 하긴 함

# 풀이
# 1. set(못들어본 사람) 를 다 입력받음 
# 2. set(못본 사람) 를 다 입력받음
# 3. 두 집합의 교집합을 구함
# 4. 구한 교집합을 list로 형변환 한 후 sort함


n, m = map(int, input().split())

no_listen = []
no_see = []

for _ in range(n):
    no_listen.append(input())

for _ in range(m):
    no_see.append(input())

no_see_listen = sorted(list(set(no_listen) & set(no_see)))

print(len(no_see_listen))
for name in no_see_listen:
    print(name)


# 후기
# 시간이 3.8초,, 2초 초과?? 
# 입력저장 변수타입을 set로 해서 input 받을때마다 add로 해봤는데 set.add()는 시간복잡도가 너무 큼 6.8초 나옴
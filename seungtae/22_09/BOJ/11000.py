import sys
input = sys.stdin.readline

s = []
e = []
for i in range(int(input())):
    start, end = map(int, input().split())
    s.append(start)     # 스타트 따로 모으기
    e.append(end)       # 엔드 따로 모으기
s.sort()            # 정렬
e.sort()            # 정렬

max_count = 0
count = 0

s_i = 0         # 스타트 인덱스
e_i = 0         # 엔드 인덱스
while s_i < len(s):     # 스타트 인덱스가 끝에 도달할때까지 while문 동작
    if s[s_i] < e[e_i]:         # 스타트 인덱스의 값이 엔드 인덱스의 값보다 작으면
        count += 1                          # 강의가 하나 열림
        s_i += 1                            # 스타트 인덱스 증가 => 다음 강의 시작 시간으로 이동
        max_count = max(max_count, count)   # 강의실 개수 최대값 검증
    else:                       # 엔드 인덱스의 강의 시간이 스타트 인덱스의 강의시간보다 크거나 같으면
        count -= 1                          # 강의 하나 끝남
        e_i += 1                            # 엔드 인덱스 증가 => 다음 강의 끝 시간으로 이동
print(max_count)
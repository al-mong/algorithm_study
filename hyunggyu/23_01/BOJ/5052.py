import sys
input = sys.stdin.readline

# test 개수
T = int(input())

for t in range(T):
    # n : 전화번호 개수
    n = int(input())
    # tel : 1-10자리수 전화번호
    tel = list(input().rstrip() for _ in range(n))
    tel.sort()
    
    # print(tel)
    # 짧은 수로 모두 비교 브루투포스
    result = True
     
    for i in range(n-1):
        if tel[i] in tel[i+1][:len(tel[i])]:
            result = False
            break
        if not result:
            break
                
            
    
    if result:
        print('YES')
    else:
        print('NO')
    
    
    
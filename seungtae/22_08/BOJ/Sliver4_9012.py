# 풀이

# 빈 리스트를 만들고 '(' 가 들어오면 리스트에 append, ')' 가 들어오면 리스트에 들어있던 '('를 pop() 한다.

# VPS가 아닌 경우는 2가지로 요약한다.

# 1. for 문을 다 돌고 난 후 리스트의 길이가 0이 아닐 때
# 2. pop을 할 '(' 가 없는데 ')'가 들어온 경우 리스트의 길이를 증가시키고 for문을 탈출(break)

# for 문을 다 돌고 나서 길이를 쟀을 때 길이가 0이면 VPS, 1이상이면 not VPS이다  


T = int(input())

for test_case in range(T):
    ps = list(input())
    vps = []
    for p in ps:
        if p == '(':
            vps.append(p)
        else:
            if len(vps) == 0:
                vps.append(1)
                break
            else:
                vps.pop()
    
    if len(vps):
        print("NO")
    else:
        print("YES")
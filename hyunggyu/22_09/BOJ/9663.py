# n, n 체스판 위에 n개의 퀸을 넣았을 때 서로 공격할 수 없게 배치하는 방법의 수
n = int(input())
chess = [0]*n # 한 열에 모두 배치하겠다.

result = 0
def put(j): # 행이 하나씩 내려간다면
    global result
    if j == n: # 모든 행이 종료되면
        result += 1
        return
    for i in range(1,n-1): # 앞에서 부터 한개씩 배치
        chess[j] = i # 세로로 두는것을 방지 세로의 j를 인덱스
        ck = True
        for k in range(j): # 앞에 있는 행을 비교했을 때
            if chess[j] == chess[k] or abs(chess[j]-chess[k]) == abs(j-k):# 행에 열이 같거나 대각선으로 만나는 경우
                ck = False
                break
        if ck:
            put(j+1)
put(0)
print(result)

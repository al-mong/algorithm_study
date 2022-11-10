import sys
input = sys.stdin.readline

def f(x, y, k):
    global ans
    print(f'x: {x}, y: {y}, k: {k}')
    for d in range(3):   
        if (k == 0 and d == 1) or (k == 1 and d == 0):
            continue
        else:
            if x + dd[d][0] == n-1 and y + dd[d][1] == n-1:
                ans += 1
            
            if d != 2:
                if n > x + dd[d][0] and n > y + dd[d][1] and nums[x + dd[d][0]][y + dd[d][1]] == 0:
                    f(x + dd[d][0], y + dd[d][1], d)
            else:
                if n > x + 1  and n > y + 1:
                    if nums[x][y + 1] == 0 and  nums[x + 1][y] == 0 and nums[x + 1][y + 1] == 0:
                        f(x + 1, y + 1, d)

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]
dd = [(0,1),(1,0),(1,1)]

nums[0][0] = 1
nums[0][1] = 1
ans = 0

if nums[n-1][n-1] == 1:
    ans = 0
else:
    f(0,1,1)

print(ans)
# deque lotate 써서 돌리고돌리고 하면 되지 않을까 싶기도 하고
# 3-9-3-9-3-9 이거 확인해서 돌아가야 함
# 한번에 돌아야되나봄 ㅇㅇ;
from collections import deque
from sys import stdin; input = stdin.readline

# 어떤 톱니바퀴가 도는지 확인해주는 함수
def cogSpin(num):
    spin_list[num] = 1
    if num == 1:
        if not spin_list[2]:
            if cogs[1][2] != cogs[2][6]:
                cogSpin(2)

    elif num == 2:
        if not spin_list[1]:
            if cogs[1][2] != cogs[2][6]:
                cogSpin(1)
        
        if not spin_list[3]:
            if cogs[2][2] != cogs[3][6]:
                cogSpin(3)

    elif num == 3:
        if not spin_list[2]:
            if cogs[2][2] != cogs[3][6]:
                cogSpin(2)
        
        if not spin_list[4]:
            if cogs[3][2] != cogs[4][6]:
                cogSpin(4)

    elif num == 4:
        if not spin_list[3]:
            if cogs[3][2] != cogs[4][6]:
                cogSpin(3)



# cog1, cog2, cog3, cog4 = [deque(map(int,input().rstrip())) for _ in range(4)]
cogs = [0] + [deque(map(int,input().rstrip())) for _ in range(4)]
print(cogs)

N = int(input())
for _ in range(N):
    cog, cnt = map(int,input().split())
    spin_list = [0,0,0,0,0]
    cogSpin(cog)

    for i in range(1,5):
        if spin_list[i]:
            if cog%2 == i%2:
                cogs[i].rotate(cnt)
            else:
                cogs[i].rotate(-cnt)

print(cogs[1][0]+(cogs[2][0]*2)+(cogs[3][0]*4)+(cogs[4][0]*8))
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

from collections import defaultdict

node_l = defaultdict(int)
node_r = defaultdict(int)
prim = defaultdict(int)



def pretree(root, next):
    if root > next:
        node_l[root] = next
        prim[next] = root # 부모 찾기 용도
    else:
        if  next < prim[root] or prim[root] == 0:
            node_r[root]
        else:
            root = prim[root]
            pretree(root, next)
root = 0
while True:
    try:
        if root:
            root = int(input())
            next = int(input())
        else:
            next = int(input())
    except:
        break
            
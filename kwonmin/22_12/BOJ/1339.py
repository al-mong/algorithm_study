# greedy하게
# original + 뒤집은거. -> 뒤집어야 자릿수나옴
from sys import stdin; input=stdin.readline
from collections import defaultdict

N = int(input())
original = []
rev = []
alp = defaultdict(int)
alp_value = defaultdict(int)
res = 0
now = 9
for _ in range(N):
    a = input().rstrip()
    original.append(a)


for origin in original:
    for i in range(len(origin), 0, -1):
        alp[origin[len(origin)-i]] += 10**i

alp_v = list(alp.items())
alp_v.sort(key=lambda x:x[1], reverse=True)
for a, _ in alp_v:
    alp_value[a] = now
    now -= 1

for origin in original:
    st = []
    for o in origin:
        st.append(str(alp_value[o]))
    res += int(''.join(st))

print(res)
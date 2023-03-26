# 저장할 때 가공하자
# 단어를 넣는게 아니라 각 알파벳 갯수 세서 넣어놓자
# 그럼 갯수 안되는 애들 다 컷하기 더 편할듯?

from sys import stdin; input=stdin.readline
from collections import defaultdict

str_list = []
while True:
    str = input().rstrip()
    alps = defaultdict(int)
    if str=="-":
        break
    for s in str:
        alps[s] += 1
    str_list.append(alps)

while True:
    alp_dict = defaultdict(int) # 받은 필드값
    res_dict = defaultdict(int) # 결과 넣는곳
    field = input().rstrip()
    if field == '#':
        break
    for f in field:
        alp_dict[f] += 1
        res_dict[f] = 0
    for st in str_list:
        for alp, cnt in st.items(): # 만약 만들 수 없는 단어일 경우
            if alp_dict[alp] < cnt:
                break
        else:
            # 만들 수 있을 경우, 키값만 카운팅하면 될 듯
            for alp, _ in st.items():
                res_dict[alp] += 1

    res_value = res_dict.values()
    minv = min(res_value)
    maxv = max(res_value)
    mink = [k for k,v in res_dict.items() if v == minv]
    maxk = [k for k,v in res_dict.items() if v == maxv]
    mink.sort()
    maxk.sort()
    res_min = "".join(mink)
    res_max = "".join(maxk)
    print(res_min, minv, res_max, maxv)


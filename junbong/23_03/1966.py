# 230307
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, target = map(int, input().split())
    docs = list(map(int, input().split()))
    docs_sorted = sorted(docs)
    q = deque([(i, docs[i]) for i in range(len(docs))])
    cnt = 0

    while q:
        doc = q.popleft()
        for other_doc in q:
            if other_doc[1] > doc[1]:
                q.append(doc)
                break
        else:
            cnt += 1
            if doc[0] == target:
                print(cnt)

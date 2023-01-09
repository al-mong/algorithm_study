from sys import stdin; input=stdin.readline
from collections import defaultdict

N = int(input())

nodes = defaultdict(list)

conn = [0]*(N+1) # 연결된 노드 갯수
leafs = []
res = 0
for _ in range(N-1): # 간선 갯수 N-1개
    stt, end = map(int,input().split())
    nodes[stt].append(end) # 양쪽으로 잇기
    nodes[end].append(stt)
    conn[stt] += 1
    conn[end] += 1



for i in range(1,N+1): # 리프노드 리스트에 담기
    if conn[i] == 1:
        leafs.append(i)

while leafs: # 리프노드 순회하기
    x = leafs.pop()
    for i in nodes[x]: # 리프노드와 이어진 노드 확인
        for j in nodes[i]: # 리프노드와 연결 끊기
            nodes[j].remove(i)
            conn[j] -= 1
            if conn[j] == 1: # 끊었는데 새로운 리프노드가 된다면 추가하기
                leafs.append(j)
        res += 1
        nodes[i].clear()
print(res)

# 220825
import sys

'''
모든 노드가 연결되어있기 때문에
노드가 n개라고 했을 때
타야하는 비행기 종류의 최소 개수는 n - 1개이다.
스타형으로 되어있어도 그냥 n - 1
비행기의 '종류'이기 때문에
'''

input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    N, M = map(int, input().split())
    for i in range(M):
        a, b = map(int, input().split())
    print(N - 1)
# 221217

'''
너비를 c에 관한 식이나
c를 너비에 관한 식으로 고쳐야 한다.
'''

import sys; input = sys.stdin.readline

x, y, c = map(float, input().split())
s, e = 0, min(x, y)  # 너비(아랫변)가 직각삼각형의 빗변보다 클 수는 없다.

while e - s > 1e-3:
    width = (s + e) / 2.0
    x_h = (x ** 2 - width ** 2) ** 0.5
    y_h = (y ** 2 - width ** 2) ** 0.5
    c_cand = (x_h * y_h) / (x_h + y_h)
    if c_cand > c:  # c_cand가 실제 c보다 높다는 것은 계산된 너비가 실제 너비보다 좁다는 것을 의미
        s = width  # 따라서 시작점을 더 크게 잡는다.
    else:
        e = width

print(width)

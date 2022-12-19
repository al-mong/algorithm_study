x, y, c = map(float, input().split())
if y > x:
    x, y = y, x

s, e, w = 0.000001, y, 0.5*y
# 0 < w < y

# 이분 탐색
while True:
    l = (x**2 - w**2)**0.5
    r = (y**2 - w**2)**0.5
    수식 = w * l / (l + r) * r / w
    tmp_c = round(수식, 6)
    # print(tmp_c)
    if tmp_c == c:
        print(f'{round(w, 3):.3f}')
        break
    elif tmp_c > c:
        s = w
        w = 0.5 * (e + s)
    elif tmp_c < c:
        e = w
        w = 0.5 * (e + s)
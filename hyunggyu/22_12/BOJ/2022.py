# x는 오하 왼상
# y는 오상 왼하
# c는 x,y의 교차점 높이
# 소수점 6자리까지 가능 <= 3,000,000,000
x,y,c = map(float, input().split())
# 범위를 줄이자
if x > y:
    x,y = y,x
# y가 무조건 크도록 만들었다. -> w의 범위는 x보다 작아진다.
# 2진 탐색으로 찾기
left = 0
right = x
while (abs(right-left) > 1e-3):
    w = (right + left)/2
    cx = (x*x - w*w)**(1/2)
    cy = (y*y - w*w)**(1/2)
    pre_c = (cx*cy)/(cx+cy)

    if (pre_c > c):
        left = w
        # 범위를 늘리기
    else:
        right = w
        # 범위를 좁히기
print(right)

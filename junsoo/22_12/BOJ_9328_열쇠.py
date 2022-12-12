'''
1. dfs체크를 하고
2. 문에 막히면 막힌 좌표 저장
3. 전부 탐색한 뒤 막혔던 부분으로 돌아가서 dfs 재실행
'''

def dfs(stack):
    global result
    while stack:
        x, y = stack.pop()

        if ground[x][y] == '*':
            continue
        elif ground[x][y] == '$':
            ground[x][y] = '*'
            result += 1
            for dx, dy in d:
                if 0 <= x + dx < h and 0 <= y + dy < w:
                    stack.append((x + dx, y + dy))
        elif ground[x][y] == '.':
            ground[x][y] = '*'
            for dx, dy in d:
                if 0 <= x + dx < h and 0 <= y + dy < w:
                    stack.append((x + dx, y + dy))
        else:
            if ground[x][y].isupper():  # 대문자면
                if ground[x][y].lower() in key:   # 열쇠가 있으면
                    ground[x][y] = '*'
                    for dx, dy in d:
                        if 0 <= x+dx < h and 0 <= y+dy < w:
                            stack.append((x+dx, y+dy))
                else:   # 열쇠가 없으면
                    if check.get(ground[x][y]):   # 이미 값이 있으면
                        check[ground[x][y]].add((x, y))
                    else:   # 없던 값이면
                        check[ground[x][y]] = {(x, y)}
            else:   # 소문자면
                key.add(ground[x][y])
                ground[x][y] = '*'
                for dx, dy in d:
                    if 0 <= x + dx < h and 0 <= y + dy < w:
                        stack.append((x + dx, y + dy))

testcase = int(input())

d = ((0, 1), (1, 0), (-1, 0), (0, -1))

for _ in range(testcase):
    result = 0
    h, w = map(int, input().split())
    # h = 세로, w = 가로

    ground = []
    for i in range(h):
        ground.append(list(input()))
    # print(ground)

    key = set(input())
    # print(key)

    check = dict()
    # 열쇠가 없을 때 좌표 저장소
    # {대문자: {좌표}}

    # 겉부터 둘러보기
    outline = []
    for i in range(h):
        outline.append((i, 0))
        outline.append((i, w-1))
    for i in range(1, w - 1):
        outline.append((0, i))
        outline.append((h-1, i))

    dfs(outline)

    # 열쇠 주웠는지 확인
    while True:
        escape = 0
        for k, v in check.items():
            if k.lower() in key:
                dfs(list(v))
                del check[k]
                escape = -10    # 임의의 낮은 값
                break
            escape += 1

        if escape == len(check.keys()):
            break

    print(result)
    print(key)
    for i in range(h):
        print(ground[i])

'''
1
15 15
**$*.**********
****.*******$**
****B.$****b.**
$*****c*****.**
*C$.*****fD..**
*$*xd******.**$
$.C********A.**
**h********.AA.
***************
***.i**********
***.***.K$*****
*k.$$I.$*******
******.$..j***$
*******D*******
****$**F*******
za
'''
def isSame(x, y):
    remove = 0
    if arr[x][y] == arr[x][y+1]:
        if arr[x][y] == arr[x+1][y]:
            if arr[x][y] == arr[x+1][y+1]:
                if arr2[x][y] == 0:
                    arr2[x][y] = -1
                    remove += 1
                if arr2[x][y+1] == 0:
                    arr2[x][y+1] = -1
                    remove += 1
                if arr2[x+1][y] == 0:
                    arr2[x+1][y] = -1
                    remove += 1
                if arr2[x+1][y+1] == 0:
                    arr2[x+1][y+1] = -1
                    remove += 1
    return remove

def solution(m, n, board):
    global arr, arr2
    answer = 0
    arr = []
    arr2 = [[0 for _ in range(n)] for _ in range(m)]

    for b in board:
        arr.append(list(b))

    count = 0
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] != 0:
                    count += isSame(i, j)

        if count != 0:
            answer += count
            count = 0
        else:
            break

        for y in range(n): # 01234
            for x in range(m-1, -1, -1): # 3210
                if arr2[x][y] == -1:
                    arr[x][y] = 0
                    for z in range(x, -1, -1):
                        if arr2[z][y] == 0:
                            arr[x][y] = arr[z][y]
                            arr[z][y] = 0
                            arr2[z][y] = -1
                            break

        arr2 = [[0 for _ in range(n)] for _ in range(m)]

    return answer
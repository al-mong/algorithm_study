'''
첫째 줄에 학생의 수 N(8 ≤ N ≤ 10,000,000)이 주어진다.

둘째 줄부터 N개의 줄에는 학생들의 성적이 무작위로 주어진다.
성적은 최소 0점부터 최대 100점까지 0.001 점 단위로 부여된다.  float

하위 7명의 성적을 점수가 낮은 순으로 각 줄마다 출력한다.
하위 7명의 성적의 커트 라인에 동점자가 있을 경우에도 7명만 출력을 하면 된다.
'''
import sys

def merge(input_list):                                                      # 병합 정렬 재귀 형식
    if len(input_list) == 1:
        return input_list
    elif len(input_list) == 2:
        if input_list[0] > input_list[1]:                                   # 앞이 크면 뒤집어 준다.
            input_list[0], input_list[1] = input_list[1], input_list[0]
            return input_list
        else:
            return input_list
    else:                                                                   # 길이가 3 이상일 떄
        left = input_list[:len(input_list) // 2]
        right = input_list[len(input_list) // 2:]
        left = merge(left)                                                  # left 오름차순 정렬
        right = merge(right)                                                # rigth 오름차순 정렬

        new_list = [0 for i in range(len(input_list))]                      # 새 값을 받아 줄 리스트
        leftnum = left.pop()
        rightnum = right.pop()
        for i in range(len(new_list)-1, -1, -1):                            # 뒤에서 뽑아 쓰니깐 뒤에서부터 집어넣는다
            if leftnum < rightnum:                                          # 큰놈을 new_list 뒤에 넣는다
                new_list[i] = rightnum
                if len(right) > 0:
                    rightnum = right.pop()
                else:                                                       # right를 다 썼으면 left를 앞에 붙임
                    new_list = left + [leftnum] + new_list[i:]
                    break
            else:
                new_list[i] = leftnum
                if len(left) > 0:
                    leftnum = left.pop()
                else:
                    new_list = right + [rightnum] + new_list[i:]
                    break

        return new_list


n = int(sys.stdin.readline())                    # print(n, type(n[0])) = ['8'] <class 'str'>

score = []
for i in range(n):
    score.append(float(sys.stdin.readline()))

score = merge(score)

for i in range(7):
    print('{:.3f}'.format(score[i]))
'''
8
0.000
0.001
1.212
1531354.121
211155.115
15141.121
123135.225
12123.121
'''
'''
첫째 줄에 학생의 수 N(8 ≤ N ≤ 10,000,000)이 주어진다.

둘째 줄부터 N개의 줄에는 학생들의 성적이 무작위로 주어진다.
성적은 최소 0점부터 최대 100점까지 0.001 점 단위로 부여된다.  float

하위 7명의 성적을 점수가 낮은 순으로 각 줄마다 출력한다.
하위 7명의 성적의 커트 라인에 동점자가 있을 경우에도 7명만 출력을 하면 된다.
'''
import sys

n = int(sys.stdin.readline())

score = []
for i in range(n):
    score.append(float(sys.stdin.readline()))

score.sort()

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
'''
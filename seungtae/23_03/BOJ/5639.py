import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# 서브트리 찾기
def find_subtree(n_list):
    # 노드가 비어있으면 리턴
    if n_list == []:
        return

    # 노드가 하나일 때 분기
    if len(n_list) == 1:
        subtree1 = [n_list[0]]
        subtree2 = []
        subtree3 = []
    #  노드가 두개 이상일 때 분기
    else:
        root = n_list[0]
        for i in range(1, len(n_list)):
            if n_list[i] > root:
                break

        if n_list[i] < root:
            i += 1

        subtree1 = [root]
        subtree2 = n_list[1:i]
        subtree3 = n_list[i:]

    # left 트리의 원소가 1개이면 출력
    if len(subtree2) == 1:
        print(subtree2[0])
    # 그렇지 않으면 서브트리 재탐색
    else:
        find_subtree(subtree2)

    # right 트리의 원소가 1개이면 출력
    if len(subtree3) == 1:
        print(subtree3[0])
    # 그렇지 않으면 서브트리 재탐색
    else:
        find_subtree(subtree3)

    # root 트리의 원소가 1개이면 출력
    if len(subtree1) == 1:
        print(subtree1[0])
    else:
        find_subtree(subtree1)

node_list = []
while True:
    try:
        node_list.append(int(sys.stdin.readline()))
    except:
        break

find_subtree(node_list)
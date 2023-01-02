import itertools

def solution(k, dungeons):
    length = len(dungeons)
    arr = list(range(length))
    order = list(itertools.permutations(arr, length))

    my_max = 0
    for i in order:
        cnt = 0
        k_copy = k
        for j in i:
            if k_copy >= dungeons[j][0]:
                if k_copy - dungeons[j][1] >= 0 :
                    k_copy = k_copy - dungeons[j][1]
                    cnt += 1
                else:
                    break

            else:
                break

        if my_max < cnt:
            my_max = cnt

    return my_max
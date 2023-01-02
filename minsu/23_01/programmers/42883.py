import itertools

def solution(number, k):
    num_list = list(str(number))
    num_count = len(num_list) - k
    perm = list(itertools.permutations(num_list, num_count))

    my_max = 0
    for i in perm:
        a = int(''.join(i))
        if my_max < a:
            my_max = a

    return str(my_max)

solution(1924, 2)
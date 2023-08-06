def solution(people, limit):
    answer = 0
    people.sort(key=lambda x:-x)
    left=0
    right=len(people)-1
    tmp=limit
    while left<=right:
        tmp-=people[left]
        left+=1
        if tmp>=people[right]:
            tmp-=people[right]
            right-=1
        answer += 1
        tmp = limit

    return answer
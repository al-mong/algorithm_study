def solution(people, limit):
    start = 0
    end = len(people)
    people.sort(reverse=True)
    while start < end:
        if limit - people[start] >= people[end-1]:
            end -= 1
        start += 1

    return start

print(solution([70, 50, 80, 50]	, 100))
print(solution([70, 80, 50]	, 100))
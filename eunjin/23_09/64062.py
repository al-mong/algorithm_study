def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)
    while left <= right:
        mid = (left + right) // 2
        j = 0
        jump = 0
        while j <= len(stones):
            if stones[j] - mid <= 0:
                jump += 1
            else:
                jump = 0
            if jump >= k:
                break
            j += 1
        if jump < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
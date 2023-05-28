def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx, p_idx = n - 1, n - 1  # 뒤에서 출발

    while d_idx >= 0 or p_idx >= 0:
        d_cap, p_cap = cap, cap
        max_length = 0

        # 배달
        for i in range(d_idx, -1, -1):
            if d_cap == 0:
                break

            if deliveries[i]:
                if deliveries[i] >= d_cap:  # cap보다 배달할 상자가 많거나 같은 경우
                    deliveries[i] -= d_cap
                    d_cap = 0
                else:
                    d_cap -= deliveries[i]
                    deliveries[i] = 0

                # 뒤에서 부터 봤을 때 최초로 배달하거나 픽업한 곳
                max_length = max(max_length, i + 1)

                d_idx = i  # deliveries[i]가 남았을 수도 있으니 다음 반복문을 위해 i로 저장

        for i in range(p_idx, -1, -1):
            if p_cap == 0:
                break

            if pickups[i]:
                if pickups[i] >= p_cap:
                    pickups[i] -= p_cap
                    p_cap = 0
                else:
                    p_cap -= pickups[i]
                    pickups[i] = 0

                # 뒤에서 부터 봤을 때 최초로 배달하거나 픽업한 곳
                max_length = max(max_length, i + 1)

                p_idx = i

        answer += max_length * 2

        if max_length == 0:
            break

    return answer


print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))

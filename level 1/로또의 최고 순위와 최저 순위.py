def solution(lottos, win_nums):
    order = [6, 6, 5, 4, 3, 2, 1]
    answer = []
    best = 0
    worst = 0

    for i in lottos:
        if i and i in win_nums:
            best += 1
            worst += 1
        elif i == 0:
            best += 1

    answer.append(order[best])
    answer.append(order[worst])

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

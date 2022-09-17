def solution(a, b):
    n = len(a)
    answer = 0

    for i in range(n):
        answer += a[i] * b[i]

    return answer


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))

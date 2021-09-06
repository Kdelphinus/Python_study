"""연습문제"""


def solution(n):
    answer = 1  # 자기 자신
    start = 1
    while start < n:
        tmp = 0
        for i in range(start, n):
            tmp += i
            if tmp >= n:
                break
        start += 1
        if tmp == n:
            answer += 1

    return answer


# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
print(solution(15))  # 4

"""Summer/Winter Coding(~2018)"""


def solution(n):
    ans = 0

    while n > 0:
        if n % 2:  # 홀수이면 1칸 점프
            ans += 1
            n -= 1
        else:  # 짝수이면 순간이동
            n //= 2

    return ans


# ---------------------------------------------------------
"""이진법을 이용한 풀이"""


def use_bin(n):
    return bin(n).count("1")


# 최대한 순간이동을 이용한다
print(solution(5))  # 2
print(solution(6))  # 2
print(solution(5000))  # 5

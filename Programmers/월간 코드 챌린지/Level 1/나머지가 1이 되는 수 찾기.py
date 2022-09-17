"""월간 코드 챌린지 시즌 3"""


def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i

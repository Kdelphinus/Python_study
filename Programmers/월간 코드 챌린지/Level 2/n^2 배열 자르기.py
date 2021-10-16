"""월간 코드 챌린지 시즌 3"""


def solution(n, left, right):
    answer = []

    # 시작과 끝 인덱스가 같은 행일 때
    if right - left < n and right // n == left // n:
        for i in range(left % n, right % n + 1):
            answer.append(max(i + 1, left // n + 1))
        return answer

    # 시작과 끝 인덱스가 다른 행일 때
    for i in range(left % n, n):  # 첫번째 행
        answer.append(max(left // n + 1, i + 1))

    for i in range(left // n + 1, right // n):  # 두 번째 ~ 마지막 직전 행
        for j in range(n):
            answer.append(max(i + 1, j + 1))

    for i in range(right % n + 1):  # 마지막 행
        answer.append(max(i + 1, right // n + 1))

    return answer


# -------------------------------------------------------------------------
"""아주 간단"""


def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    return answer

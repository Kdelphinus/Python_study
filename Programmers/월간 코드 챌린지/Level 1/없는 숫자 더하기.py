"""월간 코드 챌린지 시즌 3"""


def solution(numbers):
    answer = 0
    for num in range(10):
        if num not in numbers:
            answer += num
    return answer

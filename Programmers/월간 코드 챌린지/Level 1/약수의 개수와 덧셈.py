"""월간 코드 챌린지 시즌 2"""


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        if int(i ** 0.5) ** 2 == i:  # 제곱근이 정수인 것만 약수가 홀수개
            answer -= i
        else:
            answer += i

    return answer

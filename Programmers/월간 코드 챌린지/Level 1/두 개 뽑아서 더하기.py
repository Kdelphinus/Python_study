"""월간 코드 챌린지 시즌1"""


def solution(numbers):
    answer = []

    # 겹치지 않는 두 개의 숫자를 모두 더해본다
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:  # 들어있지 않는 것만 넣는다
                answer.append(numbers[i] + numbers[j])
    answer.sort()  # 정렬

    return answer

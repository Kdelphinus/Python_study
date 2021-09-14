"""월간 코드 챌린지 시즌 1"""


def solution(s):
    answer = [0, 0]  # 바꾼 횟수, 뺀 0의 개수
    while s != "1":  # "1"만 남으면 종료
        answer[1] += s.count("0")  # 뺀 0의 개수를 더한다
        s = format(s.count("1"), "b")  # 남은 1의 개수를 이진수로 바꾼다
        answer[0] += 1

    return answer

"""연습문제"""


def solution(s):
    number = [int(i) for i in s.split()]
    return f"{min(number)} {max(number)}"


print(solution("1 2 3 4"))  # "1 4"
print(solution("-1 -2 -3 -4"))  # "-4 -1"
print(solution("-1 -1"))  # "-1 -1"

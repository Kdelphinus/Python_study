"""연습문제"""


def solution(n):
    answer = []

    def hanoi(start, end, n):
        if n == 0:
            return

        other = 6 - (start + end)
        hanoi(start, other, n - 1)
        answer.append([start, end])
        hanoi(other, end, n - 1)

    hanoi(1, 3, n)
    return answer

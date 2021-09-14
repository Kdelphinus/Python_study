"""연습문제"""


def solution(n, s):
    """solution

    Args:
        n (int): 원소의 개수
        s (int): 각 원소의 합이 되어야 할 숫자

    Returns:
        answer (list): 모든 원소의 합이 s가 되면서 곱이 가장 큰 원소들이 들어있는 리스트
    """
    if n > s:  # 숫자가 가짓수보다 작으면 만들 수 없다
        return [-1]

    answer = []
    tmp = n
    # 그 숫자로 n등분한 수들의 곱이 가장 크다
    while len(answer) < n:
        answer.append(s // tmp)
        s -= answer[-1]
        tmp -= 1

    return answer


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))

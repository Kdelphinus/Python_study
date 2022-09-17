"""연습문제"""


def solution(A, B):
    """solution 배열 내, 하나는 오름차순하고 하나는 내림차순하여 곱하면 합의 값이 가장 작다

    Args:
        A (list): 주어진 배열
        B (list): 주어진 배열

    Returns:
        answer (int): 두 배열의 원소 중 하나씩 뽑아 곱한 수들의 총 합 중 최솟값
    """
    answer = 0
    A.sort()
    # B.sort(reverse = True)
    B.sort(key=lambda x: -x)

    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


print(solution([1, 4, 2], [5, 4, 4]))  # 29
print(solution([1, 2], [3, 4]))  # 10


# ----------------------------------------------------------------------------------------

"""zip을 활용"""


def use_zip(A, B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))

"""Summer/Winter Coding(~2018)"""


def solution(d, budget):
    """solution

    Args:
        d (list): 각 부서별 필요한 예산
        budget (int): 지급할 수 있는 예산

    Returns:
        i (int): 예산을 지급할 수 있는 부서
    """
    i = 0  # 인덱스 겸 예산을 지원할 수 있는 부서의 수
    while i < len(d):  # 모든 부서를 지원하면 종료
        d.sort()  # 예산이 적은 부서부터 나누어 주면 많은 부서에 할당 가능
        if d[i] > budget:  # 남은 예산이 필요한 예산보다 적으면 종료
            break

        budget -= d[i]  # 예산을 주고
        i += 1  # 인덱스 겸 지원 부서의 수 추가

    return i

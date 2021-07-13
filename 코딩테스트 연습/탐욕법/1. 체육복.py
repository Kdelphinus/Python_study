def solution(n, lost, reserve):
    """solution
    체육복을 도둑맞은 학생이 자신의 앞뒤 학생에게만 여분의 체육복을 빌릴 수 있을 때, 체육복을 입을 수 있는 학생의 최댓값

    Args:
        n (int): 총 학생 수
        lost (1d-list): 체육복을 도둑맞은 학생
        reserve (1d-list): 여분의 체육복이 있는 학생

    Returns:
        answer (int): 체육복을 입을 수 있는 학생의 최댓값
    """
    answer = 0
    cloth = [1] * (n + 1)  # 모두 1벌씩 가지고 있다
    cloth[0] = 0  # 0번째 인덱스는 안 쓸 것이기에 제외

    for i in reserve:  # 여분의 체육복을 가진 사람은 체육복 한 벌 추가
        cloth[i] += 1

    for i in lost:  # 체육복을 도둑맞은 사람은 체육복 한 벌 제거
        cloth[i] -= 1

    for i in lost:  # 도둑맞은 사람 중
        if cloth[i] == 0:  # 현재 옷이 없는 사람이면
            if i - 1 in reserve and cloth[i - 1] > 1:  # 앞에 사람이 여분이 있는지 확인
                cloth[i - 1] -= 1  # 앞에 사람 것을
                cloth[i] += 1  # 빌려옴
            elif i + 1 in reserve and cloth[i + 1] > 1:  # 뒤에 사람이 여분이 있는지 확인
                cloth[i + 1] -= 1  # 뒤에 사람 것을
                cloth[i] += 1  # 빌려옴

    for i in cloth:  # 전체 체육복 현황 파악
        if i > 0:  # 체육복을 입을 수 있다면
            answer += 1  # 명 수에 추가

    return answer


print(solution(5, [2, 3, 4], [3, 4, 5]))
print(solution(5, [2, 4], [1, 3, 5]))

"""나의 풀이"""


def solution(citations):
    citations.sort(reverse=True)
    idx = 0  # idx + 1 == citations[idx] 이상 인용된 논문의 수
    while idx < len(citations):
        if idx + 1 == citations[idx]:  # h번 이상 인용된 논문의 수와 h가 같다면 h리턴
            return idx + 1
        if idx + 1 > citations[idx]:  # h번 이상 인용된 논문의 수가 h보다 많다면 바로 직전 인덱스를 리턴
            return idx
        idx += 1
    return len(citations)  # 큰 것부터 확인했기에 답이 안나오면 논문의 길이가 답


print(solution([3, 0, 6, 1, 5]))

# -------------------------------------------------------
"""가장 간단한 답"""


def solution(citations):
    citations.sort(reverse=True)
    """
    0. 내림차순된 각 자리의 index는(1부터 시작한다고 했을 때) citations[index] 이상 인용된 논문의 수
    1. enumerate로 각각 (index, value)로 묶음, 이때 start를 1로 주어 인덱스가 1부터 시작하게 만듬
    2. 각각의 (index, value) 중 작은 값을 뽑아냄
    3. 뽑아낸 값들 중 최댓값이 h-index가 됨
    """
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution([3, 0, 6, 1, 5]))

# -------------------------------------------------------
"""또 다른 풀이"""


def solution(citations):
    citations = sorted(citations)  # 여기는 오름차순으로 정렬
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:  # h(인용된 횟수) 이상인 논문이 h개 이상일 때
            return l - i  # h리턴
    return 0  # 작은 것부터 확인했기에 답이 안나오면 h-index는 0


print(solution([3, 0, 6, 1, 5]))

"""1450 냅색문제"""
# 링크: https://ca.ramel.be/100


def __bruteforce(arr, subtotal, idx, total):
    """__bruteforce 모든 부분합을 구해주는 함수

    Args:
        arr (list): 주어진 수들이 있는 리스트
        subtotal (list): 부분합들을 저장할 리스트
        idx (int): __bruteforce를 몇 번 실행했는지 확인할 변수
        total (int): 구해진 부분합
    """
    if idx >= len(arr):  # arr만큼 함수를 실행했다면 부분합을 저장해야 한다
        subtotal.append(total)  # 부분합을 저장하고
        return  # 리턴

    __bruteforce(arr, subtotal, idx + 1, total)  # arr[idx]를 더하지 않은 부분합
    __bruteforce(arr, subtotal, idx + 1, total + arr[idx])  # arr[idx]를 더한 부분합


def __binary_search(arr, target):
    """이진 탐색 함수"""
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:  # target보다 중간값이 작다면 중간값보다 큰 부분만 확인
            start = mid + 1
        else:  # target보다 중간값이 크면 중간값보다 작은 부분만 확인
            end = mid
    return end  # target보다 작은 값들은 모두 가방에 들어갈 수 있다


def meet_in_the_middle(num, limit, objects):
    """meet_in_the_middle 알고리즘으로 냅색문제를 푸는 함수

    Args:
        num (int): 물건의 개수
        limit (int): 가져갈 수 있는 총 무게
        objects (list): 물건들의 무게

    Returns:
        cnt (int): 가져갈 수 있는 물건 조합의 수
    """
    # 주어진 리스트를 절반으로 나눈다
    a_objects = objects[: num // 2]
    b_objects = objects[num // 2 :]

    # 부분합들을 저장할 리스트
    a_subtotal = []
    b_subtotal = []

    # 나눠진 리스트들로 만들 수 있는 부분합들을 구한다
    __bruteforce(a_objects, a_subtotal, 0, 0)
    __bruteforce(b_objects, b_subtotal, 0, 0)
    b_subtotal.sort()  # 기준이 될 리스트는 정렬한다

    cnt = 0
    for a_sub in a_subtotal:
        if limit - a_sub >= 0:  # 구해진 부분합이 limit을 넘지 않는다면 가방에 넣을 수 있다
            # a_sub가 들어있는 가방에 넣을 수 있는 b_subtotal들을 찾는다
            cnt += __binary_search(b_subtotal, limit - a_sub)

    return cnt


num, limit = map(int, input().split())
objects = list(map(int, input().split()))
print(meet_in_the_middle(num, limit, objects))

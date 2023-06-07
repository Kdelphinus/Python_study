# Python3의 기본 MIN_MERGE
MIN_MERGE = 32


def cal_min_run(n: int) -> int:
    """
    MIN_MERGE / 2 ~ MIN_MERGE 사이의 값이 나오도록 계산하는 함수
    (이때, n이 MIN_MERGE보다 작다면 그대로 둔다.)
    Args:
        n: 정렬해야 할 원소의 개수

    Returns:
        n + r: 가공한 숫자
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1  # &는 AND 연산, |는 OR 연산
        n >>= 1  # 비트를 오른쪽으로 1번 이동, 즉 2로 나누는 연산
    return n + r


def insertion_sort(lst: list, left: int, right: int) -> None:
    """
    삽입 정렬 함수
    Args:
        lst: 정렬할 리스트
        left: 정렬할 범위 중 가장 왼쪽 인덱스
        right: 정렬할 할 범위 중 가장 오른쪽 인덱스

    Returns:

    """
    for i in range(left + 1, right + 1):
        j = i
        while j > left and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1


def merge(lst: list, l: int, m: int, r: int) -> None:
    """
    병합 정렬 함수
    Args:
        lst: 정렬할 리스트
        l: 정렬할 범위 중 가장 왼쪽 인덱스
        m: 정렬할 범위 중 중간 인덱스
        r: 정렬할 범위 중 가장 오른쪽 인덱스

    Returns:

    """
    # 원본 리스트를 주어진 인덱스에 따라 두 개의 리스트로 나눈다.
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(len1):
        left.append(lst[l + i])
    for i in range(len2):
        right.append(lst[m + 1 + i])

    # 나눠진 두 개의 리스트를 하나로 합치며 정렬을 진행한다.
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    # 남은 원소들을 원본 리스트에 채워준다.
    while i < len1:
        lst[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        lst[k] = right[j]
        k += 1
        j += 1


def tim_sort(lst: list) -> None:
    """
    Tim sort 함수
    Args:
        lst: 정렬할 리스트

    Returns:

    """
    n = len(lst)
    min_run = cal_min_run(n)

    # min_run 크기로 자른 sub list들을 삽입 정렬로 정렬
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(lst, start, end)

    # 삽입 정렬 한 sub list들을 합병 정렬로 합침
    size = min_run
    while size < n:
        # lst[left ~ left + size - 1]와 lst[left + size ~ left + size * 2 - 1]로 배열로 나눔
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge(lst, left, mid, right)

        size *= 2


if __name__ == "__main__":
    comment = "정렬할 숫자를 공백 구분으로 입력하세요. (ex. 3 4 2 1 5 0)\n"
    numbers = list(map(int, input(comment).split()))
    tim_sort(numbers)
    print(f"\n정렬 후\n")
    print(*numbers)

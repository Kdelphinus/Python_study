# 링크: https://www.geeksforgeeks.org/timsort/
MIN_MERGE = 32


def cal_min_run(n: int) -> int:
    """

    Args:
        n:

    Returns:

    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1  # &는 AND 연산, |는 OR 연산
        n >>= 1  # 비트를 오른쪽으로 1번 이동
    return n + r


def tim_sort(lst: list) -> None:
    n = len(lst)
    min_run = cal_min_run(n)

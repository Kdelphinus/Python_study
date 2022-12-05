import sys

INPUT = sys.stdin.readline
sys.setrecursionlimit(10**8)


def hanoi(n: int, start: int, end: int):
    """
    하노이 탑
    Args:
        n: 옮겨야 할 원판 개수
        start: 시작 위치
        end: 옮길 위치

    Returns:

    """
    other = 6 - start - end

    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, other)
    hanoi(1, start, end)
    hanoi(n - 1, other, end)


if __name__ == "__main__":
    num = int(INPUT())
    print(2**num - 1)
    if num <= 20:
        hanoi(num, 1, 3)

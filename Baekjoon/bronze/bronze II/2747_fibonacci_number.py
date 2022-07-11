import sys

INPUT = sys.stdin.readline


def fibonacci(n: int):
    if n < 2:
        return n

    prev, curr = 0, 1
    for _ in range(n - 1):
        tmp = curr
        curr += prev
        prev = tmp
    return curr


if __name__ == "__main__":
    n = int(INPUT())
    print(fibonacci(n))

# https://burningfalls.github.io/algorithm/boj-24511/
import sys
from enum import Enum

INPUT = sys.stdin.readline


class Types(Enum):
    QUEUE = 0
    STACK = 1


def append_queuestack() -> list:
    queuestack = []
    for i in range(N - 1, -1, -1):
        if TYPES[i] == Types.QUEUE.value:
            queuestack.append(QUEUESTACK[i])
            if len(queuestack) == M:
                return queuestack

    for i in ELEMENT:
        queuestack.append(i)
        if len(queuestack) == M:
            return queuestack


if __name__ == "__main__":
    N = int(INPUT())
    TYPES = list(map(int, INPUT().split()))
    QUEUESTACK = list(map(int, INPUT().split()))
    M = int(INPUT())
    ELEMENT = list(map(int, INPUT().split()))
    print(*append_queuestack())

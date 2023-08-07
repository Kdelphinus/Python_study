import sys
from collections import defaultdict

INPUT = sys.stdin.readline


def list_to_str(tmp: list) -> str:
    string = ""
    for t in tmp:
        string += str(t) + " "
    return string


def n_and_m(tmp: list) -> None:
    if len(tmp) == M:
        string = list_to_str(tmp)
        if not DICT[string]:
            print(*tmp)
            DICT[string] = True
        return

    for i, n in enumerate(NUMBERS):
        if CHECK[i] == 0:
            tmp.append(n)
            CHECK[i] = 1
            n_and_m(tmp)
            CHECK[i] = 0
            tmp.pop()


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    NUMBERS = sorted(list(map(int, INPUT().split())))
    CHECK = [0] * N
    DICT = defaultdict(bool)
    n_and_m([])

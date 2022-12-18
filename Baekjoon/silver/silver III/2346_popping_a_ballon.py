from collections import deque


def clock_wise(ballon: list, n: int) -> list:
    ballon.popleft()
    if not ballon:
        return ballon
    for _ in range(n - 1):
        tmp = ballon.popleft()
        ballon.append(tmp)
    return ballon


def counter_clock_wise(ballon: list, n: int) -> list:
    ballon.popleft()
    if not ballon:
        return ballon
    for _ in range(n):
        tmp = ballon.pop()
        ballon.appendleft(tmp)
    return ballon


def popping(ballon: list) -> list:
    ballon = deque([(i + 1, b) for i, b in enumerate(ballon)])
    pop = []

    while ballon:
        idx, move = ballon[0]
        pop.append(idx)
        flag = 1 if move < 0 else -1
        ballon = (
            clock_wise(ballon, abs(move))
            if move > 0
            else counter_clock_wise(ballon, abs(move))
        )

    return pop


if __name__ == "__main__":
    N = int(input())
    BALLON = list(map(int, input().split()))
    print(*popping(BALLON))

import sys
from collections import deque

INPUT = sys.stdin.readline


def find_sister() -> None:
    DP[N] = [0, 1]
    queue = deque([N])
    while queue:
        p = queue.popleft()
        if DP[p][0] > DP[K][0]:
            continue

        if p > 0:
            if DP[p][0] + 1 == DP[p - 1][0]:
                DP[p - 1][1] += DP[p][1]
            elif DP[p][0] + 1 < DP[p - 1][0]:
                DP[p - 1] = [DP[p][0] + 1, DP[p][1]]
                queue.append(p - 1)
        if p < 100000:
            if DP[p][0] + 1 == DP[p + 1][0]:
                DP[p + 1][1] += DP[p][1]
            elif DP[p][0] + 1 < DP[p + 1][0]:
                DP[p + 1] = [DP[p][0] + 1, DP[p][1]]
                queue.append(p + 1)
        if 0 < p <= 50000:
            if DP[p][0] + 1 == DP[p * 2][0]:
                DP[p * 2][1] += DP[p][1]
            elif DP[p][0] + 1 < DP[p * 2][0]:
                DP[p * 2] = [DP[p][0] + 1, DP[p][1]]
                queue.append(p * 2)


if __name__ == "__main__":
    N, K = map(int, INPUT().split())
    DP = [[float("inf"), 1] for _ in range(100001)]
    find_sister()
    print(DP[K][0])
    print(DP[K][1])
